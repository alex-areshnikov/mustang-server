import serial


class SerialRpi:
    def __init__(self):
        self._connection = serial.Serial("/dev/ttyS0", 9600, timeout=0)

    def print(self, message):
        if(self._connection.is_open):
            self._connection.write(f"{message}\xFF\xFF\xFF")
        else:
            print("Cannot write to serial. Connection is not open")

    def close(self):
        self._connection.close()
