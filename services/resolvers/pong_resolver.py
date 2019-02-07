class PongResolver:
    def __init__(self, _=None):
        pass

    def resolve(self, payload, keep_alive):
        if(payload.decode("utf-8") == "pong"):
            keep_alive.pong()
