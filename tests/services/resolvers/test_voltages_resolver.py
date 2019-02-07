from services.resolvers.voltages_resolver import VoltagesResolver
from services.vehicle.screen import Screen
from services.vehicle.keep_alive import KeepAlive


class TestVoltagesResolver(object):
    def test_it_resolves_payload(self):
        resolver = VoltagesResolver()
        screen = Screen(debug=True)

        payload = '{"name":"Bank 1",'
        payload += '"voltages":[2.3,4.61,6.93,9.26,11.6,13.95]}'

        resolved_payload = {
            "name": "Bank 1",
            "voltages": [2.3, 4.61, 6.93, 9.26, 11.6, 13.95]
        }

        banks_voltages = resolver.resolve(payload, KeepAlive(screen))
        assert banks_voltages == resolved_payload
