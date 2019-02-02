from services.util.config import Config


class TestConfig(object):
    def test_it_contains_config_values(self):
        config = Config()
        assert config.mqtt_host == "mustang.local"
        assert config.mqtt_port == 1883

    def test_it_handles_multiple_config_instances(self, make_config):
        config1 = make_config()
        config2 = make_config()

        config1.update(config1.SCREEN_SETTING_MAX_CELL_V, 2.25)
        config2.update(config2.SCREEN_SETTING_BRIGHTNESS, 5)

        config3 = make_config()
        assert config3.screen_setting_max_cell_v == 2.25
        assert config3.screen_setting_brightness == 5
