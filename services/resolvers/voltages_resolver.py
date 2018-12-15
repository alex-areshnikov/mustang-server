import json
from services.vehicle.lto.bank import Bank


class VoltagesResolver:
    def __init__(self, _=None):
        pass

    def resolve(self, payload):
        banks_voltages = self.__parse_payload(payload)
        for index, bank_voltages in enumerate(banks_voltages):
            bank = Bank(bank_voltages=bank_voltages,
                        bank_index=index+1)

            print(bank.to_s())

        return banks_voltages

    # private

    def __parse_payload(self, payload):
        return json.loads(payload)
