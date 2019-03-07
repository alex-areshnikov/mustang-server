from services.util.config import Config


class TrunkLightsSetting:
    def __init__(self, config=Config()):
        self._config = config
        self._value = config.screen_setting_trunk_lights

    def increase(self):
        self._toggle()

    def decrease(self):
        self._toggle()

    def _toggle(self):
        self._value = "OFF" if self._value == "ON" else "ON"
        self._config.update(Config.SCREEN_SETTING_TRUNK_LIGHTS, self._value)
