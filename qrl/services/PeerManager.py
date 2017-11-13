import threading
from time import time, sleep

import grpc

from qrl.core import logger, config
from qrl.generated import qrl_pb2
from qrl.generated.qrl_pb2_grpc import P2PAPIStub


class PeerMetadata(object):
    DISCOVERY_THRESHOLD_SECS = 10
    STABILITY_THRESHOLD_SECS = 2

    def __init__(self, conn_addr):
        self.connected_since = time()
        self.peers_refreshed_at = None
        self.conn_addr = conn_addr
        self.channel = grpc.insecure_channel(conn_addr)
        self.stub = P2PAPIStub(self.channel)
        self.node_info = None

    @property
    def peers_needs_refresh(self):
        return self.peers_refreshed_at is None or time() - self.peers_refreshed_at > self.DISCOVERY_THRESHOLD_SECS

    @property
    def is_stable(self):
        return (time() - self.connected_since > self.STABILITY_THRESHOLD_SECS) and self.node_info is not None


class PeerManager(object):
    TIMEOUT_SECS = 2
    REFRESH_CYCLE_SECS = 3

    def __init__(self, qrlnode):
        self._peers = dict()

        self.qrlnode = qrlnode
        self._lock = threading.Lock()
        self.thread = threading.Thread(target=self._maintain_peers)
        self.thread.daemon = True
        self.thread.start()
        # TODO: Create a bloom filter (as a black list) to avoid frequent reconnections
        # TODO: Define a banning time to avoid reconnecting to certain ips

    @property
    def peer_count(self):
        with self._lock:
            return len(self._peers)

    @property
    def stable_peer_count(self):
        with self._lock:
            return sum(1 for v in self._peers.values() if v.is_stable)

    def add(self, addr_list):
        # FIXME Get new peers every time there is a new connection
        with self._lock:
            # FIXME: Limit amount of connections
            # FIXME: Check banning before adding
            for new_peer_ip in addr_list:
                if new_peer_ip in ['127.0.0.1', '0', '0.0.0.0']:
                    continue

                new_peer_conn_addr = '{}:9009'.format(new_peer_ip)
                if new_peer_conn_addr not in self._peers:
                    self._peers[new_peer_conn_addr] = PeerMetadata(new_peer_conn_addr)

    def remove(self, conn_list):
        with self._lock:
            for peer_conn in conn_list:
                self._peers.pop(peer_conn, None)

    def recycle(self):
        with self._lock:
            # FIXME: Flush old connections to promote change, swap peers, etc. Use hash logic
            pass

    def stable_peers(self) -> list:
        with self._lock:
            return [v for v in self._peers.values() if v.is_stable]

    def _all_peers(self):
        # FIXME: Improve this. Make a temporary copy for now
        with self._lock:
            tmp = list(self._peers.values())
        return iter(tmp)

    def _validate_peer_response(self, result: GetKnownPeersResp):
        # Validate version number
        if result.node_info.version is None:
            logger.info('Invalid version: None')
            return False

        if result.node_info.version == 'local-dev':
            return True

        # FIXME: use a regex to validate this
        if not result.node_info.version[0].isdigit():
            logger.info('Invalid address: %s', result.node_info.version)
            return False

        if result.node_info.version.startswith(config.dev.required_version):
            return True

        if result.node_info.version > config.dev.required_version:
            return True

        # TODO: Validate networkid

        logger.info('Invalid address: %s', result.node_info.version)
        return False

    def _add_peers_callback(self, response_future):
        if response_future and response_future.code() == grpc.StatusCode.OK:
            result = response_future.result()
            response_future.pm.node_info = result.node_info

            self.add((peer.ip for peer in result.known_peers))      # Add all peers

            if self._validate_peer_response(result):
                return True

        self.remove([response_future.pm.conn_addr])

    def _update_state_callback(self, response_future):
        if response_future and response_future.code() == grpc.StatusCode.OK:
            result = response_future.result()
            response_future.pm.node_info = result.node_info

            if self._validate_peer_response(result):
                return True

        self.remove([response_future.pm.conn_addr])

    def _maintain_peers(self):
        while True:
            try:
                for peer_metadata in self._all_peers():
                    if peer_metadata.peers_needs_refresh:
                        f = peer_metadata.stub.GetKnownPeers.future(qrl_pb2.GetKnownPeersReq(),
                                                                    timeout=self.TIMEOUT_SECS)
                        f.pm = peer_metadata
                        f.add_done_callback(self._add_peers_callback)
                    else:
                        f = peer_metadata.stub.GetNodeState.future(qrl_pb2.GetNodeStateReq(),
                                                                   timeout=self.TIMEOUT_SECS)
                        f.pm = peer_metadata
                        f.add_done_callback(self._update_state_callback)

                # FIXME: QRLNode should probably depend on this
                tmp = []
                for peer_metadata in self.stable_peers():
                    addr = peer_metadata.conn_addr.split(':')[0]
                    tmp.append(addr)

                #self.qrlnode.update_peer_addresses(tmp)

                sleep(self.REFRESH_CYCLE_SECS)
                self.recycle()
            except Exception as e:
                logger.exception(e)
