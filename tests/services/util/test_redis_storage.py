from services.util.redis_storage import RedisStorage


class TestRedisStorage(object):
    def test_it_stores_and_reads_value(self):
        storage = RedisStorage(db=1, erase_data=True)
        assert storage.get('somekey') is None
        storage.set('mykey', 'hello')
        assert storage.get('mykey') == b'hello'
