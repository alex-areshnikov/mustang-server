from services.util.communicators.serial_rpi import SerialRpi as SerialCommunicator
from services.util.communicators.stdout import Stdout as StdoutCommunicator
from services.vehicle.screen_renderers.settings_renderer import SettingsRenderer
from services.vehicle.screen_renderers.bank_renderer import BankRenderer
from services.vehicle.screen_listener.frame_listener import FrameListener
from services.vehicle.lto.banks_comparator import BanksComparator


class Screen:
    LOGO_PAGE = "LogoPage"
    VOLTAGES_PAGE = "VoltagesPage"

    SCREEN_PAGE_IDS = {
        LOGO_PAGE: 0,
        VOLTAGES_PAGE: 1,
        SettingsRenderer.SETTINGS_PAGE: 2
    }

    def __init__(self, config, debug=False):
        self._page = 0
        self._communicator = (StdoutCommunicator() if debug else SerialCommunicator())
        self._bank_renderer = BankRenderer(self._communicator)
        self._config = config
        self._charging = True
        self._banks_comparator = BanksComparator()
        self._publisher = None

    def initialize(self, publisher):
        self._publisher = publisher

        self._communicator.start()
        self._communicator.print("baud=115200")
        self._communicator.close()
        self._communicator.start(115200)

        self.page(self.VOLTAGES_PAGE)
        self._frame_listener = FrameListener(self._communicator, self._frame_callback)
        self._frame_listener.start()
        self._render_brightness()
        self._publish_trunk_lights()

    def page(self, page_object):
        self._page = self._page_id(page_object)
        self._communicator.print(f"page {self._page}")
        self._render_charging()

    def render_bank(self, bank):
        if(self._page != self._page_id(self.VOLTAGES_PAGE)):
            return

        bank.calculate_overcharged(self._config.screen_setting_max_cell_v)
        is_overcharged = self._banks_comparator.compare_overcharged(bank)

        if(is_overcharged != BanksComparator.NO_CHANGE_CHARGE_TRANSITION):
            self._charging = not is_overcharged
            self._render_charging()

        self._bank_renderer.render(bank)

    def close(self):
        self._communicator.close()

    def _render_brightness(self):
        self._communicator.print(f"dim={self._config.screen_setting_brightness * 10}")

    def _render_charging(self):
        self._publish_charging()

        if(self._page == self._page_id(self.VOLTAGES_PAGE)):
            self._communicator.print(f"vis iDischarge,{0 if self._is_charging_enabled() else 1}")

    def _publish_charging(self):
        if(self._publisher):
            self._publisher.charging(1 if self._is_charging_enabled() else 0)

    def _publish_trunk_lights(self):
        if(self._publisher):
            self._publisher.trunk_lights(0 if self._config.screen_setting_trunk_lights else 1)

    def _is_charging_enabled(self):
        return self._charging and self._config.screen_setting_charging

    def _page_id(self, page_object):
        return self.SCREEN_PAGE_IDS.get(page_object, 0)

    def _frame_callback(self, actions={}):
        if(actions.get("page_id")):
            self._page = actions["page_id"]
            self._render_charging()

        if(actions.get("settings_update")):
            self._config.reload()
            self._render_brightness()
            self._publish_charging()
            self._publish_trunk_lights()
