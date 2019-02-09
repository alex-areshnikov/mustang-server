class PongResolver:
    def __init__(self, _=None):
        pass

    def resolve(self, payload, resources):
        if(payload.decode("utf-8") == "pong"):
            resources["keep_alive"].pong()
