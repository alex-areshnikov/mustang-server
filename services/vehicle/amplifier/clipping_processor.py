class ClippingProcessor:
    NORMAL_STATUS = 1
    CLIPPING_STATUS = 2
    CLIPPING_VOLTAGE_PIONT = 400

    def __init__(self):
        self._clipping_status = self.NORMAL_STATUS
        self._is_status_changed = False

    def is_clipping(self):
        return self._clipping_status == self.CLIPPING_STATUS

    def is_status_changed(self):
        return self._is_status_changed

    def process_incoming_voltage(self, voltage_str):
        voltage = int(voltage_str)

        new_status = (self.CLIPPING_STATUS if voltage > self.CLIPPING_VOLTAGE_PIONT else self.NORMAL_STATUS)
        self._is_status_changed = new_status != self._clipping_status
        self._clipping_status = new_status
