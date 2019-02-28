from services.vehicle.settings.trunk_lights_setting import TrunkLightsSetting


class TestTrunkLightsSetting(object):
    def test_it_toggles_on_increase_decrease(self, config):
        setting = TrunkLightsSetting(config=config)
        assert not getattr(config, config.SCREEN_SETTING_TRUNK_LIGHTS)
        setting.increase()
        assert getattr(config, config.SCREEN_SETTING_TRUNK_LIGHTS)
        setting.increase()
        assert not getattr(config, config.SCREEN_SETTING_TRUNK_LIGHTS)
        setting.decrease()
        assert getattr(config, config.SCREEN_SETTING_TRUNK_LIGHTS)
        setting.decrease()
        assert not getattr(config, config.SCREEN_SETTING_TRUNK_LIGHTS)
