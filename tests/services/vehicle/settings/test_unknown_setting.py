from services.vehicle.settings.unknown_setting import UnknownSetting


class TestChargingSetting(object):
    def test_it_responds_to_increase_decrease(self, config, capfd):
        setting = UnknownSetting(config=config)
        setting.increase()
        setting.decrease()

        out, err = capfd.readouterr()
        assert out == ("Pressed: increase on unknown setting\n"
                       "Pressed: decrease on unknown setting\n")
