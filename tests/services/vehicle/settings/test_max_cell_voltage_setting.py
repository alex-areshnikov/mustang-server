from services.vehicle.settings.max_cell_voltage_setting import MaxCellVoltageSetting


class TestMaxCellVoltageSetting(object):
    def test_it_increases_voltage(self, config):
        setting = MaxCellVoltageSetting(config=config)
        setting.increase()
        assert getattr(config, config.SCREEN_SETTING_MAX_CELL_V) == 2.7

    def test_it_decreases_voltage(self, config):
        setting = MaxCellVoltageSetting(config=config)
        setting.decrease()
        assert getattr(config, config.SCREEN_SETTING_MAX_CELL_V) == 2.6

    def test_it_does_not_increase_above_maximum(self, config):
        config.update(config.SCREEN_SETTING_MAX_CELL_V, 3.0)
        setting = MaxCellVoltageSetting(config=config)
        setting.increase()
        assert getattr(config, config.SCREEN_SETTING_MAX_CELL_V) == 3.0

    def test_it_does_not_decrease_below_minimum(self, config):
        config.update(config.SCREEN_SETTING_MAX_CELL_V, 1.5)
        setting = MaxCellVoltageSetting(config=config)
        setting.decrease()
        assert getattr(config, config.SCREEN_SETTING_MAX_CELL_V) == 1.5
