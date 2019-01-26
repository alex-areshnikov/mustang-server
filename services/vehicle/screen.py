from services.util.printers.serial_rpi import SerialRpi as SerialPrinter
from services.util.printers.stdout import Stdout as StdoutPrinter


class Screen:
    def __init__(self, debug=False):
        self._printer = (StdoutPrinter() if debug else SerialPrinter())

    def initialize(self):
        self._printer.start()
        self._printer.print("baud=115200")
        self._printer.close()
        self._printer.start(115200)
        self.page(1)

    def page(self, page_number=0):
        self._printer.print(f"page {page_number}")

    def render_bank(self, bank):
        self._printer.print(f"b{bank.number}label.txt=\"{bank.name}\"")
        self._printer.print(f"b{bank.number}total.txt=\"{bank.voltage}v\"")

        for index, voltage in enumerate(bank.flat_voltages):
            scr_varialbe = f"b{bank.number}s{index+1}"
            self._printer.print(f"{scr_varialbe}.txt=\"{voltage}v\"")

    def close(self):
        self._printer.close()
