import pytest
from services.resolvers.default_resolver import DefaultResolver


class TestDefaultResolver(object):
    def test_it_says_cannot_resolve_topic(self):
        resolver = DefaultResolver("unknown/topic")
        expected_message = "Resolver not found for topic \"unknown/topic\". "
        expected_message += "Payload: incoming_payload"
        assert resolver.resolve("incoming_payload") == expected_message
