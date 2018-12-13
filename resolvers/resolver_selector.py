from default_resolver import DefaultResolver
from voltages_resolver import VoltagesResolver


class ResolverSelector:
    TOPIC_RESOLVERS = {
        "vehicle/lto/voltages": VoltagesResolver
    }

    def __init__(self, topic):
        self.topic = topic

    def resolver(self):
        self.TOPIC_RESOLVERS.get(self.topic, DefaultResolver)(self.topic)
