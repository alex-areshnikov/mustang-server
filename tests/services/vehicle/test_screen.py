from services.vehicle.screen import Screen
from services.vehicle.lto.bank import Bank


class TestScreen(object):
    def test_it_initializes_screen(self, capfd):
        screen = Screen(debug=True)
        screen.initialize(listen_screen=False)
        out, err = capfd.readouterr()
        assert out == ("Started connection @9600\n"
                       "baud=115200\n"
                       "Connection closed\n"
                       "Started connection @115200\n"
                       "page 1\n")

    def test_it_sets_page(self, capfd):
        screen = Screen(debug=True)
        screen.page(6)
        out, err = capfd.readouterr()
        assert out == ("page 6\n")

    def test_it_renders_bank(self, capfd):
        screen = Screen(debug=True)
        voltages = [2.3, 4.61, 6.93, 9.26, 11.6, 13.95]
        bank = Bank(bank_number=2, bank_voltages={"voltages": voltages})
        screen.render_bank(bank)
        out, err = capfd.readouterr()
        assert out == ("b2label.txt=\"Bank 2\"\n"
                       "b2total.txt=\"13.95v\"\n"
                       "b2s1.txt=\"2.3v\"\n"
                       "b2s2.txt=\"2.31v\"\n"
                       "b2s3.txt=\"2.32v\"\n"
                       "b2s4.txt=\"2.33v\"\n"
                       "b2s5.txt=\"2.34v\"\n"
                       "b2s6.txt=\"2.35v\"\n")

    def test_it_closes_connection(self, capfd):
        screen = Screen(debug=True)
        screen.close()
        out, err = capfd.readouterr()
        assert out == ("Connection closed\n")

    def test_it_renders_settings(self, config, capfd):
        screen = Screen(debug=True)
        screen.render_settings()
        out, err = capfd.readouterr()
        assert out == ("Settings.g_charging.txt=\"ON\"\n"
                       "Settings.g_max_cell_v.txt=\"2.65\"\n"
                       "Settings.g_brightness.txt=\"10\"\n")
