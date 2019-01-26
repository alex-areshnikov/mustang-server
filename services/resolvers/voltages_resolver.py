import json
from services.vehicle.lto.bank import Bank


class VoltagesResolver:
    def __init__(self, _=None):
        pass

    def resolve(self, payload, screen):
        bank_voltages = self._parse_payload(payload)
        bank = Bank(bank_voltages=bank_voltages, bank_number=1)
        screen.render_bank(bank)

        return bank_voltages

    # private

    def _parse_payload(self, payload):
        return json.loads(payload)
