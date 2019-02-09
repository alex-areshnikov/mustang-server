from unittest.mock import patch

from services.vehicle.keep_alive import KeepAlive
from services.vehicle.screen import Screen


class TestKeepAlive(object):
    @patch.object(Screen, 'render_bank')
    def test_it_pings_and_pongs(self, mock_render_bank, screen):
        keep_alive = KeepAlive(screen)
        keep_alive.ping()
        keep_alive.pong()
        keep_alive.ping()
        assert mock_render_bank.call_count == 1
