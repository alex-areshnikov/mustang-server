class BlankBank:
    def __init__(self, bank_number):
        self._bank_number = bank_number
        self._name = "-"
        self._flat_voltages = ['-.--']*6

    @property
    def name(self):
        return self._name

    @property
    def voltage(self):
        return "--.--"

    @property
    def flat_voltages(self):
        return self._flat_voltages

    @property
    def number(self):
        return self._bank_number
