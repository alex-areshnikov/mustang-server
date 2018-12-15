from services.resolvers.default_resolver import DefaultResolver
from services.resolvers.voltages_resolver import VoltagesResolver


class ResolverSelector:
    TOPIC_RESOLVERS = {
        "vehicle/lto/voltages": VoltagesResolver
    }

    def __init__(self, topic):
        self.topic = topic

    def resolver(self):
        resolver_class = self.TOPIC_RESOLVERS.get(self.topic, DefaultResolver)
        return resolver_class(self.topic)
