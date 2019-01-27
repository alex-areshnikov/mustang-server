class UnknownFrameProcessor:
    def __init__(self, frame):
        self._frame = frame

    def process(self):
        print(f"Frame processor not found for \"{self._frame}\"")
