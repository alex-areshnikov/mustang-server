from services.vehicle.frame_processors.button_press_frame_processor import ButtonPressFrameProcessor


class TestButtonPressFrameProcessor(object):
    def test_it_processes_charging_increase_frame(self, capfd):
        frame = bytes(b'\x65\x02\x0A\x00\xFF\xFF\xFF')
        processor = ButtonPressFrameProcessor(frame)
        processor.process()
        out, err = capfd.readouterr()
        assert out == "Pressed: charging increase\n"

    def test_it_processes_charging_decrease_frame(self, capfd):
        frame = bytes(b'\x65\x02\x09\x00\xFF\xFF\xFF')
        processor = ButtonPressFrameProcessor(frame)
        processor.process()
        out, err = capfd.readouterr()
        assert out == "Pressed: charging decrease\n"

    def test_it_processes_max_cell_v_increase_frame(self, capfd):
        frame = bytes(b'\x65\x02\x06\x00\xFF\xFF\xFF')
        processor = ButtonPressFrameProcessor(frame)
        processor.process()
        out, err = capfd.readouterr()
        assert out == "Pressed: max_cell_v increase\n"

    def test_it_processes_max_cell_v_decrease_frame(self, capfd):
        frame = bytes(b'\x65\x02\x07\x00\xFF\xFF\xFF')
        processor = ButtonPressFrameProcessor(frame)
        processor.process()
        out, err = capfd.readouterr()
        assert out == "Pressed: max_cell_v decrease\n"

    def test_it_processes_brightness_increase_frame(self, capfd):
        frame = bytes(b'\x65\x02\x0D\x00\xFF\xFF\xFF')
        processor = ButtonPressFrameProcessor(frame)
        processor.process()
        out, err = capfd.readouterr()
        assert out == "Pressed: brightness increase\n"

    def test_it_processes_brightness_decrease_frame(self, capfd):
        frame = bytes(b'\x65\x02\x0C\x00\xFF\xFF\xFF')
        processor = ButtonPressFrameProcessor(frame)
        processor.process()
        out, err = capfd.readouterr()
        assert out == "Pressed: brightness decrease\n"
