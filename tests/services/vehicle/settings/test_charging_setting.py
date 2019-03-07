from services.vehicle.settings.charging_setting import ChargingSetting


class TestChargingSetting(object):
    def test_it_toggles_on_increase_decrease(self, config):
        setting = ChargingSetting(config=config)
        assert config.screen_setting_charging == "ON"
        setting.increase()
        assert config.screen_setting_charging == "OFF"
        setting.increase()
        assert config.screen_setting_charging == "ON"
        setting.decrease()
        assert config.screen_setting_charging == "OFF"
        setting.decrease()
        assert config.screen_setting_charging == "ON"
