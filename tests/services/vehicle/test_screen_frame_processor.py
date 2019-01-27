from services.vehicle.screen_frame_processor import ScreenFrameProcessor


class TestScreenFrameProcessor(object):
    def test_it_recognizes_button_press_frame(self):
        frame = bytes(b'\x65\x02\x0A\x00\xFF\xFF\xFF')
        screen_frame_processor = ScreenFrameProcessor()
        assert screen_frame_processor._frame_type(frame) == ScreenFrameProcessor.BUTTON_PRESS_FRAME

    def test_it_does_not_recognize_frame(self):
        frame = bytes(b'\x65\x02\x0A\x00\xFF\xAF\xFF')
        screen_frame_processor = ScreenFrameProcessor()
        assert screen_frame_processor._frame_type(frame) == ScreenFrameProcessor.UNKNOWN_FRAME
