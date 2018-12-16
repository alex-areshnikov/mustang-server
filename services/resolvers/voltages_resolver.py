import json
from services.vehicle.lto.bank import Bank


class VoltagesResolver:
    def __init__(self, _=None):
        pass

    def resolve(self, payload, screen):
        banks_voltages = self._parse_payload(payload)
        for index, bank_voltages in enumerate(banks_voltages):
            bank = Bank(bank_voltages=bank_voltages,
                        bank_number=index+1)

            screen.print(bank)

        return banks_voltages

    # private

    def _parse_payload(self, payload):
        return json.loads(payload)
