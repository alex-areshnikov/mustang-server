class Bank:
    def __init__(self, bank_number, bank_voltages={}):
        self._bank_number = bank_number
        self._name = bank_voltages.get("name", f"Bank {bank_number}")
        self._voltages = bank_voltages.get("voltages", [])
        self._overcharged_cells = [False] * len(self._voltages)
        self._flat_voltages = None

    @property
    def name(self):
        return self._name

    @property
    def voltage(self):
        return self.voltages[-1]

    @property
    def voltages(self):
        return self._voltages

    @property
    def min_cell_voltage(self):
        return min(self.flat_voltages)

    @property
    def max_cell_voltage(self):
        return max(self.flat_voltages)

    @property
    def flat_voltages(self):
        if not self._flat_voltages:
            self._calc_flat_voltages()

        return self._flat_voltages

    @property
    def number(self):
        return self._bank_number

    def is_overcharged(self):
        return any(self._overcharged_cells)

    def is_cell_overcharged(self, cell_id):
        return self._overcharged_cells[cell_id]

    def calculate_overcharged(self, max_cell_voltage):
        for index, voltage in enumerate(self.flat_voltages):
            self._overcharged_cells[index] = voltage >= max_cell_voltage

    def to_s(self):
        return f"({self.voltage}v) {self.name} voltages {self.flat_voltages}"

    # private

    def _calc_flat_voltages(self):
        rev_voltages = self._voltages[::-1]

        deltas = [x - y for x, y in zip(rev_voltages, rev_voltages[1:])]
        deltas = [round(delta, 2) for delta in deltas]

        self._flat_voltages = [self._voltages[0]] + deltas[::-1]
