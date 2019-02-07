from services.resolvers.resolver_selector import ResolverSelector


class TestResolverSelector(object):
    def test_it_selects_voltages_resolver(self):
        topic = "vehicle/lto/voltages"

        selector = ResolverSelector(topic)
        resolver = selector.resolver()

        assert resolver.__class__.__name__ == "VoltagesResolver"

    def test_it_selects_pong_resolver(self):
        topic = "vehicle/lto/keep_alive"

        selector = ResolverSelector(topic)
        resolver = selector.resolver()

        assert resolver.__class__.__name__ == "PongResolver"

    def test_it_selects_default_resolver(self):
        topic = "unknown/topic"

        selector = ResolverSelector(topic)
        resolver = selector.resolver()

        assert resolver.__class__.__name__ == "DefaultResolver"
