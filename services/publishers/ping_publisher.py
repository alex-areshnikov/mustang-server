import threading
import time
from services.resolvers.resolver_selector import ResolverSelector


class PingPublisher:
    def __init__(self, client, keep_alive):
        self._client = client
        self._keep_alive = keep_alive
        self._thread = threading.Thread(target=self._start)

    def run(self):
        self._thread.start()

    def _start(self):
        while True:
            self._client.publish(ResolverSelector.KEEP_ALIVE_TOPIC, 'ping')
            self._keep_alive.ping()
            time.sleep(self._keep_alive.INTERVAL_SECONDS)
