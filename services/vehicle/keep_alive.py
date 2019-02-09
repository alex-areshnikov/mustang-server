from services.vehicle.lto.blank_bank import BlankBank
from datetime import datetime


class KeepAlive:
    INTERVAL_SECONDS = 2
    MAX_NO_RESPONSE_SECONDS = 3

    def __init__(self, screen):
        self._screen = screen
        self._status_alive = True
        self._ping_timestamp = datetime.now()
        self._pong_timestamp = None

    def ping(self):
        if(self._is_alive()):
            self._process_alive()
        else:
            self._process_dead()

        self._ping_timestamp = datetime.now()

    def pong(self):
        self._pong_timestamp = datetime.now()

    def _process_alive(self):
        if(self._status_alive):
            return

        self._status_alive = True

    def _process_dead(self):
        if(not self._status_alive):
            return

        self._status_alive = False
        self._screen.render_bank(BlankBank(bank_number=1))

    def _is_alive(self):
        if(self._pong_timestamp is None):
            return False

        return (self._pong_timestamp - self._ping_timestamp).seconds <= self.MAX_NO_RESPONSE_SECONDS
