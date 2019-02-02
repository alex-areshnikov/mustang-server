from services.vehicle.settings.charging_setting import ChargingSetting


class TestChargingSetting(object):
    def test_it_toggles_on_increase_decrease(self, config):
        setting = ChargingSetting(config=config)
        assert getattr(config, config.SCREEN_SETTING_CHARGING)
        setting.increase()
        assert not getattr(config, config.SCREEN_SETTING_CHARGING)
        setting.increase()
        assert getattr(config, config.SCREEN_SETTING_CHARGING)
        setting.decrease()
        assert not getattr(config, config.SCREEN_SETTING_CHARGING)
        setting.decrease()
        assert getattr(config, config.SCREEN_SETTING_CHARGING)
