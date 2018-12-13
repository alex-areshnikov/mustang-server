class DefaultResolver:
    def __init__(self, topic):
        self.topic = topic

    def resolve(self, payload):
        message = "Resolver not found for topic \""
        message += self.topic + "\". Payload: " + payload

        print(message)
        return message
