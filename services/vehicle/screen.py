from services.util.communicators.serial_rpi import SerialRpi as SerialCommunicator
from services.util.communicators.stdout import Stdout as StdoutCommunicator
from services.vehicle.screen_renderers.settings_renderer import SettingsRenderer
from services.vehicle.screen_listener.frame_listener import FrameListener
from services.vehicle.screen_renderers.bank_renderer import BankRenderer
from services.vehicle.lto.blank_bank import BlankBank


class Screen:
    LOGO_PAGE = "LogoPage"
    VOLTAGES_PAGE = "VoltagesPage"

    SCREEN_PAGE_IDS = {
        LOGO_PAGE: 0,
        VOLTAGES_PAGE: 1,
        SettingsRenderer.SETTINGS_PAGE: 2
    }

    def __init__(self, debug=False):
        self._page = 0
        self._communicator = (StdoutCommunicator() if debug else SerialCommunicator())
        self._bank_renderer = BankRenderer(self._communicator)

    def initialize(self):
        self._communicator.start()
        self._communicator.print("baud=115200")
        self._communicator.close()
        self._communicator.start(115200)

        self.page(self.VOLTAGES_PAGE)
        self._frame_listener = FrameListener(self._communicator, self._frame_callback)
        self._frame_listener.start()
        self.render_bank(BlankBank(bank_number=1))

    def page(self, page_object):
        self._page = self._page_id(page_object)
        self._communicator.print(f"page {self._page}")

    def render_bank(self, bank):
        if(self._page != self._page_id(self.VOLTAGES_PAGE)):
            return

        self._bank_renderer.render(bank)

    def close(self):
        self._communicator.close()

    def _page_id(self, page_object):
        return self.SCREEN_PAGE_IDS.get(page_object, 0)

    def _frame_callback(self, page_id=None):
        if(page_id):
            self._page = page_id
