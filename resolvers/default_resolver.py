class DefaultResolver:
    def __init__(self, topic):
        self.topic = topic

    def resolve(self, payload):
        message = "Resolver not found for topic \"" + self.topic + "\". Payload: " + payload
        print(message)
        return message