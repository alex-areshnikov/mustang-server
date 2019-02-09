from services.vehicle.screen_listener.frame_processors.page_change_processor import PageChangeProcessor


class TestPageChangeProcessor(object):
    def test_it_processes_charging_increase_frame(self):
        def callback(actions):
            assert actions == {'page_id': 2}

        frame = bytes(b'\xAA\xAA\x02\xFF\xFF\xFF')
        processor = PageChangeProcessor(frame)
        processor.process(callback)
