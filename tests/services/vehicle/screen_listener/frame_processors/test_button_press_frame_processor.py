from unittest.mock import patch

from services.vehicle.screen_listener.frame_processors.button_press_frame_processor import ButtonPressFrameProcessor
from services.vehicle.settings.charging_setting import ChargingSetting
from services.vehicle.settings.max_cell_voltage_setting import MaxCellVoltageSetting
from services.vehicle.settings.brightness_setting import BrightnessSetting
from services.vehicle.settings.trunk_lights_setting import TrunkLightsSetting


class TestButtonPressFrameProcessor(object):
    @patch.object(ChargingSetting, 'increase')
    def test_it_processes_charging_increase_frame(self, mock_method, frame_callback):
        frame = bytes(b'\x65\x02\x0A\x00\xFF\xFF\xFF')
        processor = ButtonPressFrameProcessor(frame)
        processor.process(frame_callback)
        mock_method.assert_called_once()

    @patch.object(ChargingSetting, 'decrease')
    def test_it_processes_charging_decrease_frame(self, mock_method, frame_callback):
        frame = bytes(b'\x65\x02\x09\x00\xFF\xFF\xFF')
        processor = ButtonPressFrameProcessor(frame)
        processor.process(frame_callback)
        mock_method.assert_called_once()

    @patch.object(MaxCellVoltageSetting, 'increase')
    def test_it_processes_max_cell_v_increase_frame(self, mock_method, frame_callback):
        frame = bytes(b'\x65\x02\x06\x00\xFF\xFF\xFF')
        processor = ButtonPressFrameProcessor(frame)
        processor.process(frame_callback)
        mock_method.assert_called_once()

    @patch.object(MaxCellVoltageSetting, 'decrease')
    def test_it_processes_max_cell_v_decrease_frame(self, mock_method, frame_callback):
        frame = bytes(b'\x65\x02\x07\x00\xFF\xFF\xFF')
        processor = ButtonPressFrameProcessor(frame)
        processor.process(frame_callback)
        mock_method.assert_called_once()

    @patch.object(BrightnessSetting, 'increase')
    def test_it_processes_brightness_increase_frame(self, mock_method, frame_callback):
        frame = bytes(b'\x65\x02\x0D\x00\xFF\xFF\xFF')
        processor = ButtonPressFrameProcessor(frame)
        processor.process(frame_callback)
        mock_method.assert_called_once()

    @patch.object(BrightnessSetting, 'decrease')
    def test_it_processes_brightness_decrease_frame(self, mock_method, frame_callback):
        frame = bytes(b'\x65\x02\x0C\x00\xFF\xFF\xFF')
        processor = ButtonPressFrameProcessor(frame)
        processor.process(frame_callback)
        mock_method.assert_called_once()

    @patch.object(TrunkLightsSetting, 'increase')
    def test_it_processes_brightness_increase_frame(self, mock_method, frame_callback):
        frame = bytes(b'\x65\x02\x12\x00\xFF\xFF\xFF')
        processor = ButtonPressFrameProcessor(frame)
        processor.process(frame_callback)
        mock_method.assert_called_once()

    @patch.object(TrunkLightsSetting, 'decrease')
    def test_it_processes_brightness_decrease_frame(self, mock_method, frame_callback):
        frame = bytes(b'\x65\x02\x11\x00\xFF\xFF\xFF')
        processor = ButtonPressFrameProcessor(frame)
        processor.process(frame_callback)
        mock_method.assert_called_once()
