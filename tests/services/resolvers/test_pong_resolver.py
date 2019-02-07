from unittest.mock import patch

from services.resolvers.pong_resolver import PongResolver
from services.vehicle.keep_alive import KeepAlive


class TestPongResolver(object):
    @patch.object(KeepAlive, 'pong')
    def test_it_resolves_pong(self, mock_pong):
        resolver = PongResolver()
        resolver.resolve(b'pong', KeepAlive(None))
        resolver.resolve(b'ponxgg', KeepAlive(None))
        mock_pong.assert_called_once()
