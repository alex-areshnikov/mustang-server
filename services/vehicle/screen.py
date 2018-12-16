from services.util.printers.serial_rpi import SerialRpi as SerialPrinter
from services.util.printers.stdout import Stdout as StdoutPrinter


class Screen:
    def __init__(self, debug=False):
        self._printer = (StdoutPrinter() if debug else SerialPrinter())

    def page(self, page_number=0):
        self._printer.print(f"page {page_number}")

    def print(self, bank):
        self._printer.print(f"b{bank.number}label.txt=\"{bank.name}\"")
        self._printer.print(f"b{bank.number}total.txt=\"{bank.voltage}v\"")

        for index, voltage in enumerate(bank.flat_voltages):
            scr_varialbe = self._scr_varialbe_for(
                bunk_number=bank.number, cell_number=index+1)

            self._printer.print(f"{scr_varialbe}.txt=\"{voltage}v\"")

    def close(self):
        self._printer.close()

    # private

    def _scr_varialbe_for(self, bunk_number, cell_number):
        return f"b{bunk_number}s{cell_number}"
