from services.util.config import Config
from services.vehicle.settings.helpers.min_max_setting import MinMaxSetting


class BrightnessSetting:
    def __init__(self, config=Config()):
        self._config = config
        self._setting_key = config.SCREEN_SETTING_BRIGHTNESS
        self._min_max_setting = MinMaxSetting(initial_value=getattr(self._config, self._setting_key))

    def increase(self):
        self._min_max_setting.increase()
        self._config.update(self._setting_key, self._min_max_setting.value)

    def decrease(self):
        self._min_max_setting.decrease()
        self._config.update(self._setting_key, self._min_max_setting.value)
