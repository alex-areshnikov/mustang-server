from services.util.config import Config
from services.vehicle.settings.helpers.min_max_setting import MinMaxSetting


class MaxCellVoltageSetting:
    def __init__(self, config=Config()):
        self._config = config
        self._setting_key = config.SCREEN_SETTING_MAX_CELL_V
        value = getattr(self._config, self._setting_key)
        self._min_max_setting = MinMaxSetting(min=1.5, max=3.0, step=0.05, initial_value=value)

    def increase(self):
        self._min_max_setting.increase()
        self._config.update(self._setting_key, self._min_max_setting.value)

    def decrease(self):
        self._min_max_setting.decrease()
        self._config.update(self._setting_key, self._min_max_setting.value)
