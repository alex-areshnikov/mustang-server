from unittest.mock import patch

from services.vehicle.screen_frame_processor import ScreenFrameProcessor
from services.vehicle.frame_processors.button_press_frame_processor import ButtonPressFrameProcessor
from services.vehicle.frame_processors.page_change_processor import PageChangeProcessor
from services.vehicle.frame_processors.unknown_frame_processor import UnknownFrameProcessor


class TestScreenFrameProcessor(object):
    @patch.object(ButtonPressFrameProcessor, 'process')
    @patch.object(ButtonPressFrameProcessor, '__init__', return_value=None)
    def test_it_recognizes_button_press_frame(self, mock_init, mock_process):
        frame = bytes(b'\x65\x02\x0A\x00\xFF\xFF\xFF')
        screen_frame_processor = ScreenFrameProcessor()
        screen_frame_processor.process(frame, None)
        mock_init.assert_called_once_with(frame)
        mock_process.assert_called_once()

    @patch.object(PageChangeProcessor, 'process')
    @patch.object(PageChangeProcessor, '__init__', return_value=None)
    def test_it_recognizes_page_change_frame(self, mock_init, mock_process):
        frame = bytes(b'\xAA\xAA\x02\xFF\xFF\xFF')
        screen_frame_processor = ScreenFrameProcessor()
        screen_frame_processor.process(frame, None)
        mock_init.assert_called_once_with(frame)
        mock_process.assert_called_once()

    @patch.object(UnknownFrameProcessor, 'process')
    @patch.object(UnknownFrameProcessor, '__init__', return_value=None)
    def test_it_does_not_recognize_frame(self, mock_init, mock_process):
        frame = bytes(b'\x65\x02\x0A\x00\xFF\xAF\xFF')
        screen_frame_processor = ScreenFrameProcessor()
        screen_frame_processor.process(frame, None)
        mock_init.assert_called_once_with(frame)
        mock_process.assert_called_once()
