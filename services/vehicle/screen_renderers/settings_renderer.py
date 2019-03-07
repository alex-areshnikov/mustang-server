from services.util.config import Config


class SettingsRenderer:
    SETTINGS_PAGE = "SettingsPage"

    def __init__(self, communicator):
        self._communicator = communicator

    def render(self, config=Config()):
        self._communicator.print(f"{self.SETTINGS_PAGE}.g_charging.txt=\"{config.screen_setting_charging}\"")
        self._communicator.print(f"{self.SETTINGS_PAGE}.g_max_cell_v.txt=\"{config.screen_setting_max_cell_v}\"")
        self._communicator.print(f"{self.SETTINGS_PAGE}.g_t_lights.txt=\"{config.screen_setting_trunk_lights}\"")
        self._communicator.print(f"{self.SETTINGS_PAGE}.g_brightness.txt=\"{config.screen_setting_brightness}\"")
