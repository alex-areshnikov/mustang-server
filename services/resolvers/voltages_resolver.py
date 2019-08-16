import json
from services.vehicle.lto.bank import Bank


class VoltagesResolver:
    def __init__(self, _=None):
        pass

    def resolve(self, payload, resources):
        config = resources["config"]
        screen = resources["screen"]
        overcharge_processor = resources["overcharge_processor"]

        bank_voltages = self._parse_payload(payload)

        bank = Bank(bank_voltages=bank_voltages, bank_number=1)
        bank.calculate_overcharged(config.screen_setting_max_cell_v)

        overcharge_processor.process_bank(bank.is_overcharged())

        screen.set_charging(overcharge_processor.is_charging())
        screen.render_bank(bank)

        return bank_voltages

    # private

    def _parse_payload(self, payload):
        return json.loads(payload)
