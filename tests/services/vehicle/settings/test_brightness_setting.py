from services.vehicle.settings.brightness_setting import BrightnessSetting


class TestBrightnessSetting(object):
    def test_it_increases_brightness(self, config):
        config.update(config.SCREEN_SETTING_BRIGHTNESS, 5)
        setting = BrightnessSetting(config=config)
        setting.increase()
        assert config.screen_setting_brightness == 6

    def test_it_decreases_brightness(self, config):
        setting = BrightnessSetting(config=config)
        setting.decrease()
        assert config.screen_setting_brightness == 9

    def test_it_does_not_increase_above_maximum(self, config):
        setting = BrightnessSetting(config=config)
        setting.increase()
        assert config.screen_setting_brightness == 10

    def test_it_does_not_decrease_below_minimum(self, config):
        config.update(config.SCREEN_SETTING_BRIGHTNESS, 0)
        setting = BrightnessSetting(config=config)
        setting.decrease()
        assert config.screen_setting_brightness == 0
