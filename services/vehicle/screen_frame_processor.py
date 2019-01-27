from services.util.config import Config
from services.vehicle.frame_processors.button_press_frame_processor import ButtonPressFrameProcessor
from services.vehicle.frame_processors.unknown_frame_processor import UnknownFrameProcessor


class ScreenFrameProcessor:
    BUTTON_PRESS_FRAME = 1
    UNKNOWN_FRAME = -1

    FRAME_PROCESSORS = {
        BUTTON_PRESS_FRAME: ButtonPressFrameProcessor,
        UNKNOWN_FRAME: UnknownFrameProcessor
    }

    def process(self, frame):
        processor_klass = self.FRAME_PROCESSORS.get(self._frame_type(frame), UnknownFrameProcessor)
        processor_klass(frame).process()

    def _frame_type(self, frame):
        if(frame[0:2] == bytes(b'\x65\x02') and frame[-3:] == bytes(b'\xFF\xFF\xFF')):
            return self.BUTTON_PRESS_FRAME

        return self.UNKNOWN_FRAME
