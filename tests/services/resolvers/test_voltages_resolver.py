import pytest
from services.resolvers.voltages_resolver import VoltagesResolver


class TestVoltagesResolver(object):
    def test_it_resolves_payload(self):
        resolver = VoltagesResolver()

        payload = '[{"bank_number":1,'
        payload += '"voltages":[2.3,4.61,6.93,9.26,11.6,13.95]},'
        payload += '{"bank_number":2,'
        payload += '"voltages":[2.2,4.63,7.06,9.46,11.89,14.33]}]'

        resolved_payload = [
            {
                "bank_number": 1,
                "voltages": [2.3, 4.61, 6.93, 9.26, 11.6, 13.95]
            },
            {
                "bank_number": 2,
                "voltages": [2.2, 4.63, 7.06, 9.46, 11.89, 14.33]
            }
        ]

        banks_voltages = resolver.resolve(payload)
        assert banks_voltages == resolved_payload
