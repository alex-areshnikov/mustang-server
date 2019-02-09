import pytest


class TestBank(object):
    def test_it_returns_voltages(self, bank):
        assert bank.voltages == [2.3, 4.61, 6.93, 9.26, 11.6, 13.95]
        assert bank.flat_voltages == [2.3, 2.31, 2.32, 2.33, 2.34, 2.35]

    def test_it_returns_total_voltage(self, bank):
        assert bank.voltage == 13.95

    def test_it_returns_min_max_cell_voltages(self, bank):
        assert bank.min_cell_voltage == 2.3
        assert bank.max_cell_voltage == 2.35

    def test_it_returns_bank_number(self, bank):
        assert bank.number == 2

    def test_it_returns_name(self, bank):
        assert bank.name == "Bank 2"

    def test_it_prints_self_out(self, bank):
        bank_line = "(13.95v) Bank 2 voltages "
        bank_line += "[2.3, 2.31, 2.32, 2.33, 2.34, 2.35]"
        assert bank.to_s() == bank_line

    def test_it_calculates_overcharged(self, bank):
        assert not bank.is_overcharged()
        bank.calculate_overcharged(2.33)
        assert bank.is_overcharged()
        assert not bank.is_cell_overcharged(2)
        assert bank.is_cell_overcharged(3)
        assert bank.is_cell_overcharged(4)
