from services.vehicle.settings.brightness_setting import BrightnessSetting


class TestBrightnessSetting(object):
    def test_it_increases_brightness(self, config):
        config.update(config.SCREEN_SETTING_BRIGHTNESS, 5)
        setting = BrightnessSetting(config=config)
        setting.increase()
        assert getattr(config, config.SCREEN_SETTING_BRIGHTNESS) == 6

    def test_it_decreases_brightness(self, config):
        setting = BrightnessSetting(config=config)
        setting.decrease()
        assert getattr(config, config.SCREEN_SETTING_BRIGHTNESS) == 9

    def test_it_does_not_increase_above_maximum(self, config):
        setting = BrightnessSetting(config=config)
        setting.increase()
        assert getattr(config, config.SCREEN_SETTING_BRIGHTNESS) == 10

    def test_it_does_not_decrease_below_minimum(self, config):
        config.update(config.SCREEN_SETTING_BRIGHTNESS, 0)
        setting = BrightnessSetting(config=config)
        setting.decrease()
        assert getattr(config, config.SCREEN_SETTING_BRIGHTNESS) == 0
