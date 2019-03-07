from services.util.config import Config
from services.vehicle.settings.helpers.min_max_setting import MinMaxSetting


class BrightnessSetting:
    def __init__(self, config=Config()):
        self._config = config
        self._min_max_setting = MinMaxSetting(initial_value=config.screen_setting_brightness)

    def increase(self):
        self._min_max_setting.increase()
        self._config.update(Config.SCREEN_SETTING_BRIGHTNESS, self._min_max_setting.value)

    def decrease(self):
        self._min_max_setting.decrease()
        self._config.update(Config.SCREEN_SETTING_BRIGHTNESS, self._min_max_setting.value)
