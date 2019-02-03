class PageChangeProcessor:
    PAGE_ID_INDEX = 2

    def __init__(self, frame):
        self._frame = frame

    def process(self, callback):
        callback(page_id=self._frame[self.PAGE_ID_INDEX])
