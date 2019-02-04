from services.vehicle.screen_listener.frame_processors.button_press_frame_processor import ButtonPressFrameProcessor
from services.vehicle.screen_listener.frame_processors.page_change_processor import PageChangeProcessor
from services.vehicle.screen_listener.frame_processors.unknown_frame_processor import UnknownFrameProcessor


class ScreenFrameProcessor:
    BUTTON_PRESS_FRAME = 1
    PAGE_CHANGE_FRAME = 2
    UNKNOWN_FRAME = -1

    FRAME_PROCESSORS = {
        BUTTON_PRESS_FRAME: ButtonPressFrameProcessor,
        PAGE_CHANGE_FRAME: PageChangeProcessor,
        UNKNOWN_FRAME: UnknownFrameProcessor
    }

    def process(self, frame, callback):
        processor_klass = self.FRAME_PROCESSORS.get(self._frame_type(frame), UnknownFrameProcessor)
        processor_klass(frame).process(callback)

    def _frame_type(self, frame):
        if(frame[0:1] == bytes(b'\x65') and frame[-3:] == bytes(b'\xFF\xFF\xFF')):
            return self.BUTTON_PRESS_FRAME

        if(frame[0:2] == bytes(b'\xAA\xAA') and frame[-3:] == bytes(b'\xFF\xFF\xFF')):
            return self.PAGE_CHANGE_FRAME

        return self.UNKNOWN_FRAME
