class BankRenderer:
    def __init__(self, communicator):
        self._communicator = communicator

    def render(self, bank):
        self._communicator.print(f"b{bank.number}label.txt=\"{bank.name}\"")
        self._communicator.print(f"b{bank.number}total.txt=\"{bank.voltage}v\"")

        for index, voltage in enumerate(bank.flat_voltages):
            scr_varialbe = f"b{bank.number}s{index+1}"
            self._communicator.print(f"{scr_varialbe}.txt=\"{voltage}v\"")