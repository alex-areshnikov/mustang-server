from services.vehicle.frame_processors.unknown_frame_processor import UnknownFrameProcessor


class TestUnknownFrameProcessor(object):
    def test_it_processes_charging_increase_frame(self, capfd):
        frame = bytes(b'\x01\x02\x03\x04\xAD\xAE\xAF')
        processor = UnknownFrameProcessor(frame)
        processor.process(None)
        out, err = capfd.readouterr()
        assert out == f"Frame processor not found for \"{frame}\"\n"
