from services.resolvers.default_resolver import DefaultResolver
from services.resolvers.voltages_resolver import VoltagesResolver
from services.resolvers.clipping_resolver import ClippingResolver
from services.resolvers.pong_resolver import PongResolver


class ResolverSelector:
    VOLTAGES_TOPIC = "vehicle/lto/voltages"
    KEEP_ALIVE_TOPIC = "vehicle/lto/keep_alive"
    CLIPPING_TOPIC = "vehicle/monoblock/clipping"

    def __init__(self, topic):
        self.topic = topic

    def resolver(self):
        resolver_class = self._topic_resolvers().get(self.topic, DefaultResolver)
        return resolver_class(self.topic)

    def _topic_resolvers(self):
        return {
            self.VOLTAGES_TOPIC: VoltagesResolver,
            self.KEEP_ALIVE_TOPIC: PongResolver,
            self.CLIPPING_TOPIC: ClippingResolver
        }
