from services.resolvers.clipping_resolver import ClippingResolver


class TestClippingResolver(object):
    def test_it_resolves_payload(self, screen, clipping_processor):
        resolver = ClippingResolver()
        payload = b'800'

        resolver.resolve(payload, {"screen": screen, "clipping_processor": clipping_processor})
