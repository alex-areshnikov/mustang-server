import serial


class SerialRpi:
    def __init__(self):
        self._connection = None

    def start(self, baud=9600):
        self._connection = serial.Serial("/dev/ttyS0", baud)

    def print(self, message):
        if(self._connection.is_open):
            self._connection.write(bytes(message, "ascii")+b'\xFF\xFF\xFF')
        else:
            print("Cannot write to serial. Connection is not open")

    def close(self):
        self._connection.close()
