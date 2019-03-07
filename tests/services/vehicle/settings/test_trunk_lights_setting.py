from services.vehicle.settings.trunk_lights_setting import TrunkLightsSetting


class TestTrunkLightsSetting(object):
    def test_it_toggles_on_increase_decrease(self, config):
        setting = TrunkLightsSetting(config=config)
        assert config.screen_setting_trunk_lights == "OFF"
        setting.increase()
        assert config.screen_setting_trunk_lights == "ON"
        setting.increase()
        assert config.screen_setting_trunk_lights == "OFF"
        setting.decrease()
        assert config.screen_setting_trunk_lights == "ON"
        setting.decrease()
        assert config.screen_setting_trunk_lights == "OFF"
