from services.util.config import Config


class TestConfig(object):
    def test_it_contains_config_values(self):
        config = Config()
        assert config.mqtt_host == "mustang.local"
        assert config.mqtt_port == 1883
