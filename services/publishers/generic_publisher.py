class GenericPublisher:
    CHARGING_TOPIC = "vehicle/lto/charge"

    def __init__(self, client):
        self._client = client

    def publish(self, topic, payload):
        self._client.publish(topic, payload)

    def charging(self, payload):
        self.publish(self.CHARGING_TOPIC, payload)
