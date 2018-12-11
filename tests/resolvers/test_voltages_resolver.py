import pytest
from resolvers.voltages_resolver import VoltagesResolver

class TestDefaultResolver(object):
    def test_it_resolves_payload(self):
        resolver = VoltagesResolver()
        payload = '[{"bank_number":1,"voltages":[2.4,4.69,7.06,9.46,11.92,14.31]},{"bank_number":2,"voltages":[2.2,4.63,7.06,9.46,11.89,14.33]}]'        
        resolver.resolve(payload)