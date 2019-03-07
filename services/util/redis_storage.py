import redis


class RedisStorage:
    def __init__(self, host="localhost", port=6379, db=0, erase_data=False):
        self._redis_connection = redis.Redis(host, port, db)

        if(erase_data):
            self._redis_connection.flushdb()

    def get(self, key):
        return self._redis_connection.get(key)

    def set(self, key, value):
        return self._redis_connection.set(key, value)
