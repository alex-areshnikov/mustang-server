import pytest


class TestClippingProcessor(object):
    def test_it_processes_clipping(self, clipping_processor):
        assert not clipping_processor.is_clipping()

        clipping_processor.process_incoming_voltage("20")
        assert not clipping_processor.is_status_changed()
        assert not clipping_processor.is_clipping()

        clipping_processor.process_incoming_voltage("800")
        assert clipping_processor.is_status_changed()
        assert clipping_processor.is_clipping()

        clipping_processor.process_incoming_voltage("800")
        assert not clipping_processor.is_status_changed()
        assert clipping_processor.is_clipping()

        clipping_processor.process_incoming_voltage("20")
        assert clipping_processor.is_status_changed()
        assert not clipping_processor.is_clipping()

        clipping_processor.process_incoming_voltage("20")
        assert not clipping_processor.is_status_changed()
        assert not clipping_processor.is_clipping()
