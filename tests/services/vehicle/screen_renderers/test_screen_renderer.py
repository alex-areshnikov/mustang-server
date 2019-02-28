from services.vehicle.screen_renderers.settings_renderer import SettingsRenderer
from services.util.communicators.stdout import Stdout as StdoutCommunicator


class TestSettingsRenderer(object):
    def test_it_renders_settings(self, config, capfd):
        renderer = SettingsRenderer(StdoutCommunicator())
        renderer.render(config=config)
        out, err = capfd.readouterr()
        assert out == ("SettingsPage.g_charging.txt=\"ON\"\n"
                       "SettingsPage.g_max_cell_v.txt=\"2.65\"\n"
                       "SettingsPage.g_t_lights.txt=\"OFF\"\n"
                       "SettingsPage.g_brightness.txt=\"10\"\n")
