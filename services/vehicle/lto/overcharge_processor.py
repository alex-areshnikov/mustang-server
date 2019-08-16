import datetime


class OverchargeProcessor:
    STATUS_CHANGE_DELAY_SECONDS = 15
    NORMAL_STATUS = 1
    OVERCHARGED_STATUS = 2

    def __init__(self):
        self._status = self.NORMAL_STATUS
        self._status_change_since_timestamp = None

    def process_bank(self, is_bank_overcharged):
        if((is_bank_overcharged and self._status == self.NORMAL_STATUS) or (not is_bank_overcharged and self._status == self.OVERCHARGED_STATUS)):
            self._process_status_change_counter()
            return

        self._stop_status_change_counter()

    def is_charging(self):
        self._update_status()
        return self._status == self.NORMAL_STATUS

    # private

    def _process_status_change_counter(self):
        self._update_status()

        if(self._status_change_since_timestamp is None):
            self._status_change_since_timestamp = datetime.datetime.now()

    def _update_status(self):
        if(self._is_timestamp_exceeds_status_change_delay()):
            self._status = self._status_change()
            self._stop_status_change_counter()

    def _status_change(self):
        return self.OVERCHARGED_STATUS if self._status == self.NORMAL_STATUS else self.NORMAL_STATUS

    def _stop_status_change_counter(self):
        self._status_change_since_timestamp = None

    def _is_timestamp_exceeds_status_change_delay(self):
        if(self._status_change_since_timestamp is None):
            return False

        return (datetime.datetime.now() - self._status_change_since_timestamp).total_seconds() > self.STATUS_CHANGE_DELAY_SECONDS
