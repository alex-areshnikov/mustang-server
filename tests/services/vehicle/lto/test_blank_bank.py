from services.vehicle.lto.blank_bank import BlankBank


class TestBlankBank(object):
    def test_it_returns_correct_values(self):
        bank = BlankBank(bank_number=1)
        assert bank.name == "-"
        assert bank.voltage == "--.--"
        assert bank.flat_voltages == ["-.--"]*6
        assert bank.number == 1
