class UnknownFrameProcessor:
    def __init__(self, frame):
        self._frame = frame

    def process(self, _):
        print(f"Frame processor not found for \"{self._frame}\"")
