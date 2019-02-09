from services.vehicle.lto.banks_comparator import BanksComparator
import copy


class TestBanksComparator(object):
    def test_it_compares_sequence_of_banks(self, bank):
        banks_comparator = BanksComparator()

        bank.calculate_overcharged(2.25)
        assert banks_comparator.compare_overcharged(bank)

        bank = copy.deepcopy(bank)
        bank.calculate_overcharged(2.25)
        assert banks_comparator.compare_overcharged(bank) == BanksComparator.NO_CHANGE_CHARGE_TRANSITION

        bank = copy.deepcopy(bank)
        bank.calculate_overcharged(2.65)
        assert not banks_comparator.compare_overcharged(bank)

        bank = copy.deepcopy(bank)
        bank.calculate_overcharged(2.65)
        assert banks_comparator.compare_overcharged(bank) == BanksComparator.NO_CHANGE_CHARGE_TRANSITION

        bank = copy.deepcopy(bank)
        bank.calculate_overcharged(2.25)
        assert banks_comparator.compare_overcharged(bank)
