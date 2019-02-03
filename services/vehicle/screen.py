from services.util.printers.serial_rpi import SerialRpi as SerialPrinter
from services.util.printers.stdout import Stdout as StdoutPrinter
from services.vehicle.screen_frame_processor import ScreenFrameProcessor
from services.util.config import Config

import threading
import time


class Screen:
    LOGO_PAGE = "LogoPage"
    VOLTAGES_PAGE = "VoltagesPage"
    SETTINGS_PAGE = "SettingsPage"

    SCREEN_PAGE_IDS = {
        LOGO_PAGE: 0,
        VOLTAGES_PAGE: 1,
        SETTINGS_PAGE: 2
    }

    def __init__(self, debug=False):
        self._debug = debug
        self._page = 0
        self._printer = (StdoutPrinter() if debug else SerialPrinter())
        self._screen_frame_processor = ScreenFrameProcessor()

    def initialize(self, listen_screen=True):
        self._printer.start()
        self._printer.print("baud=115200")
        self._printer.close()
        self._printer.start(115200)
        self.page(self.VOLTAGES_PAGE)

        if(not self._debug):
            self.render_settings()

        if(listen_screen):  # Not covered by tests
            self._start_listener()

    def page(self, page_object):
        self._page = self._page_id(page_object)
        self._printer.print(f"page {self._page}")

    def render_settings(self):
        config = Config()
        charging = "ON" if config.screen_setting_charging else "OFF"
        self._printer.print(f"{self.SETTINGS_PAGE}.g_charging.txt=\"{charging}\"")
        self._printer.print(f"{self.SETTINGS_PAGE}.g_max_cell_v.txt=\"{config.screen_setting_max_cell_v}\"")
        self._printer.print(f"{self.SETTINGS_PAGE}.g_brightness.txt=\"{config.screen_setting_brightness}\"")

    def render_bank(self, bank):
        if(self._page != self._page_id(self.VOLTAGES_PAGE)):
            return

        self._printer.print(f"b{bank.number}label.txt=\"{bank.name}\"")
        self._printer.print(f"b{bank.number}total.txt=\"{bank.voltage}v\"")

        for index, voltage in enumerate(bank.flat_voltages):
            scr_varialbe = f"b{bank.number}s{index+1}"
            self._printer.print(f"{scr_varialbe}.txt=\"{voltage}v\"")

    def close(self):
        self._printer.close()

    def _page_id(self, page_object):
        return self.SCREEN_PAGE_IDS.get(page_object, 0)

    def _start_listener(self):
        thread = threading.Thread(target=self._listen_screen, args=(self._printer,))
        thread.start()

    def _frame_callback(self, page_id=None):
        if(page_id):
            self._page = page_id

    def _listen_screen(self, printer):
        while printer.is_open():
            frame = printer.readframe()
            if(len(frame) > 0):
                self._screen_frame_processor.process(frame, self._frame_callback)
                self.render_settings()

            time.sleep(0.5 if self._debug else 0.1)
