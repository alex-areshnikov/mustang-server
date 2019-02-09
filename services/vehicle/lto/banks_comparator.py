class BanksComparator:
    NO_CHANGE_CHARGE_TRANSITION = None

    def __init__(self):
        self._prev_bank = None

    def compare_overcharged(self, bank):
        if(self._prev_bank is None):
            return self._store_bank_and_return(bank, bank.is_overcharged())

        if(self._prev_bank.is_overcharged() == bank.is_overcharged()):
            return self._store_bank_and_return(bank, self.NO_CHANGE_CHARGE_TRANSITION)

        return self._store_bank_and_return(bank, bank.is_overcharged())

    def _store_bank_and_return(self, bank, return_value):
        self._prev_bank = bank
        return return_value
