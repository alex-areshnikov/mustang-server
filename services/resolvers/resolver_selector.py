from services.resolvers.default_resolver import DefaultResolver
from services.resolvers.voltages_resolver import VoltagesResolver
from services.resolvers.pong_resolver import PongResolver
from services.publishers.ping_publisher import PingPublisher


class ResolverSelector:
    TOPIC_RESOLVERS = {
        "vehicle/lto/voltages": VoltagesResolver,
        PingPublisher.KEEP_ALIVE_TOPIC: PongResolver
    }

    def __init__(self, topic):
        self.topic = topic

    def resolver(self):
        resolver_class = self.TOPIC_RESOLVERS.get(self.topic, DefaultResolver)
        return resolver_class(self.topic)
