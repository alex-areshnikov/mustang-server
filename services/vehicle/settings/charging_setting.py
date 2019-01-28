from services.util.config import Config


class ChargingSetting:
    def __init__(self, config=Config()):
        self._config = config
        self._setting_key = config.SCREEN_SETTING_CHARGING
        self._value = getattr(self._config, self._setting_key)

    def increase(self):
        self._toggle()

    def decrease(self):
        self._toggle()

    def _toggle(self):
        self._value = not self._value
        self._config.update(self._setting_key, self._value)
