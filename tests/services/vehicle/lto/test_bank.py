import pytest
from services.vehicle.lto.bank import Bank


class TestBank(object):
    def test_it_returns_voltages(self):
        bank = self.bank()
        assert bank.voltages == [2.3, 4.61, 6.93, 9.26, 11.6, 13.95]

    def test_it_returns_flat_voltages(self):
        bank = self.bank()
        assert bank.flat_voltages == [2.3, 2.31, 2.32, 2.33, 2.34, 2.35]

    def test_it_returns_total_voltage(self):
        bank = self.bank()
        assert bank.voltage == 13.95

    def test_it_returns_min_max_cell_voltages(self):
        bank = self.bank()
        assert bank.min_cell_voltage == 2.3
        assert bank.max_cell_voltage == 2.35

    def test_it_returns_bank_number(self):
        bank = self.bank()
        assert bank.number == 1

    def test_it_returns_name(self):
        bank = self.bank()
        assert bank.name == "Bank 1"

    def test_it_returns_custom_name(self):
        bank = self.bank("Custom Bank Name")
        assert bank.name == "Custom Bank Name"

    def test_it_prints_self_out(self):
        bank = self.bank()
        bank_line = "(13.95v) Bank 1 voltages "
        bank_line += "[2.3, 2.31, 2.32, 2.33, 2.34, 2.35]"
        assert bank.to_s() == bank_line

    def bank(self, name=None):
        voltages = [2.3, 4.61, 6.93, 9.26, 11.6, 13.95]
        bank_voltages = {"voltages": voltages}
        if name:
            bank_voltages["name"] = name

        return Bank(bank_number=1, bank_voltages=bank_voltages)
