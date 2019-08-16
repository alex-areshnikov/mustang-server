import pytest
import datetime
from freezegun import freeze_time


class TestOverchargeProcessor(object):
    def test_it_delays_status_change(self, overcharge_processor):
        with freeze_time(datetime.datetime.now()) as frozen_datetime:
            assert overcharge_processor.is_charging()

            overcharge_processor.process_bank(True)
            assert overcharge_processor.is_charging()

            overcharge_processor.process_bank(True)
            frozen_datetime.tick(delta=datetime.timedelta(seconds=10))
            assert overcharge_processor.is_charging()

            frozen_datetime.tick(delta=datetime.timedelta(seconds=10))
            assert overcharge_processor.is_charging() is False

            frozen_datetime.tick(delta=datetime.timedelta(seconds=20))
            assert overcharge_processor.is_charging() is False

            overcharge_processor.process_bank(False)

            frozen_datetime.tick(delta=datetime.timedelta(seconds=10))
            assert overcharge_processor.is_charging() is False

            overcharge_processor.process_bank(True)
            frozen_datetime.tick(delta=datetime.timedelta(seconds=10))
            assert overcharge_processor.is_charging() is False

            overcharge_processor.process_bank(False)

            frozen_datetime.tick(delta=datetime.timedelta(seconds=10))
            assert overcharge_processor.is_charging() is False

            frozen_datetime.tick(delta=datetime.timedelta(seconds=6))
            assert overcharge_processor.is_charging()
