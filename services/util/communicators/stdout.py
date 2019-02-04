import random


class Stdout:
    def __init__(self):
        self._open = False
        self._frames_list = [
            bytes(b'\x65\x02\x09\x00\xFF\xFF\xFF'),
            bytes(b'\x65\x02\x0A\x00\xFF\xFF\xFF'),
            bytes(b'\x65\x02\x07\x00\xFF\xFF\xFF'),
            bytes(b'\x65\x02\x06\x00\xFF\xFF\xFF'),
            bytes(b'\x65\x02\x0C\x00\xFF\xFF\xFF'),
            bytes(b'\x65\x02\x0D\x00\xFF\xFF\xFF')
        ]

    def print(self, message):
        print(message)

    def start(self, baud=9600):
        print(f"Started connection @{baud}")
        self._open = True

    def is_open(self):
        return self._open

    def readframe(self):
        frame = self._frames_list[random.randrange(len(self._frames_list))]
        print(f"Received frame: {frame}")
        return frame

    def close(self):
        print("Connection closed")
        self._open = False
