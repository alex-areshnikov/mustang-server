from services.vehicle.screen import Screen


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
        screen.page(screen.SETTINGS_PAGE)
        screen.page("NonExistingPgae")
        out, err = capfd.readouterr()
        assert out == ("page 2\npage 0\n")

    def test_it_does_not_render_bank(self, bank, capfd):
        screen = Screen(debug=True)
        screen.render_bank(bank)
        out, err = capfd.readouterr()
        assert out == ""

    def test_it_renders_bank(self, bank, capfd):
        screen = Screen(debug=True)
        screen.page(screen.VOLTAGES_PAGE)
        screen.render_bank(bank)
        out, err = capfd.readouterr()
        assert out == ("page 1\n"
                       "b2label.txt=\"Bank 2\"\n"
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
        assert out == ("SettingsPage.g_charging.txt=\"ON\"\n"
                       "SettingsPage.g_max_cell_v.txt=\"2.65\"\n"
                       "SettingsPage.g_brightness.txt=\"10\"\n")
