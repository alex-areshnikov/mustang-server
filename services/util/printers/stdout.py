class Stdout:
    def print(self, message):
        print(message)

    def start(self, baud=9600):
        print(f"Started connection @{baud}")

    def close(self):
        print("Connection closed")
