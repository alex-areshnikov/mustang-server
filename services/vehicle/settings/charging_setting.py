from services.util.config import Config


class ChargingSetting:
    def __init__(self, config=Config()):
        self._config = config
        self._value = config.screen_setting_charging

    def increase(self):
        self._toggle()

    def decrease(self):
        self._toggle()

    def _toggle(self):
        self._value = "OFF" if self._value == "ON" else "ON"
        self._config.update(Config.SCREEN_SETTING_CHARGING, self._value)
