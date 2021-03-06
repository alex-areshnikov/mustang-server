from unittest.mock import patch

from services.vehicle.screen import Screen
from services.vehicle.screen_renderers.settings_renderer import SettingsRenderer
from services.vehicle.screen_listener.frame_listener import FrameListener


class TestScreen(object):
    @patch.object(SettingsRenderer, 'render')
    @patch.object(FrameListener, 'start')
    @patch.object(Screen, 'render_bank')
    def test_it_initializes_screen(self, mock_render_bank, mock_start_listener, mock_render, screen, capfd):
        screen.initialize(None)
        out, err = capfd.readouterr()
        assert out == ("Started connection @9600\n"
                       "baud=115200\n"
                       "Connection closed\n"
                       "Started connection @115200\n"
                       "page 1\n"
                       "vis iDischarge,0\n"
                       "dim=100\n"
                       "b1label.txt=\"\"\n")

    def test_it_sets_page(self, screen, capfd):
        screen.page(screen.VOLTAGES_PAGE)
        screen.page(SettingsRenderer.SETTINGS_PAGE)
        screen.page("NonExistingPgae")
        out, err = capfd.readouterr()
        assert out == ("page 1\n"
                       "vis iDischarge,0\n"
                       "page 2\n"
                       "page 0\n")

    def test_it_does_not_render_bank(self, bank, screen, capfd):
        screen.render_bank(bank)
        out, err = capfd.readouterr()
        assert out == ""

    def test_it_renders_bank(self, bank, screen, capfd):
        screen.page(screen.VOLTAGES_PAGE)
        screen.render_bank(bank)
        out, err = capfd.readouterr()
        assert out == ("page 1\n"
                       "vis iDischarge,0\n"
                       "b2total.txt=\"13.95v\"\n"
                       "b2s1.txt=\"2.3v\"\n"
                       "b2s1.pco=65535\n"
                       "b2s2.txt=\"2.31v\"\n"
                       "b2s2.pco=65535\n"
                       "b2s3.txt=\"2.32v\"\n"
                       "b2s3.pco=65535\n"
                       "b2s4.txt=\"2.33v\"\n"
                       "b2s4.pco=65535\n"
                       "b2s5.txt=\"2.34v\"\n"
                       "b2s5.pco=65535\n"
                       "b2s6.txt=\"2.35v\"\n"
                       "b2s6.pco=65535\n")

    def test_it_renders_discharge_and_bank(self, bank, screen, capfd):
        screen.page(screen.VOLTAGES_PAGE)
        screen.set_charging(False)
        screen.render_bank(bank)
        out, err = capfd.readouterr()
        assert out == ("page 1\n"
                       "vis iDischarge,0\n"
                       "vis iDischarge,1\n"
                       "b2total.txt=\"13.95v\"\n"
                       "b2s1.txt=\"2.3v\"\n"
                       "b2s1.pco=65535\n"
                       "b2s2.txt=\"2.31v\"\n"
                       "b2s2.pco=65535\n"
                       "b2s3.txt=\"2.32v\"\n"
                       "b2s3.pco=65535\n"
                       "b2s4.txt=\"2.33v\"\n"
                       "b2s4.pco=65535\n"
                       "b2s5.txt=\"2.34v\"\n"
                       "b2s5.pco=65535\n"
                       "b2s6.txt=\"2.35v\"\n"
                       "b2s6.pco=65535\n")

    def test_it_renders_blank_bank(self, blank_bank, screen, capfd):
        screen.page(screen.VOLTAGES_PAGE)
        screen.render_bank(blank_bank)
        out, err = capfd.readouterr()
        assert out == ("page 1\n"
                       "vis iDischarge,0\n"
                       "b2total.txt=\"--.--v\"\n"
                       "b2s1.txt=\"-.--v\"\n"
                       "b2s1.pco=65535\n"
                       "b2s2.txt=\"-.--v\"\n"
                       "b2s2.pco=65535\n"
                       "b2s3.txt=\"-.--v\"\n"
                       "b2s3.pco=65535\n"
                       "b2s4.txt=\"-.--v\"\n"
                       "b2s4.pco=65535\n"
                       "b2s5.txt=\"-.--v\"\n"
                       "b2s5.pco=65535\n"
                       "b2s6.txt=\"-.--v\"\n"
                       "b2s6.pco=65535\n")

    def test_it_renders_clipping(self, screen, capfd):
        screen.render_clipping(True)
        screen.page(screen.VOLTAGES_PAGE)
        screen.render_clipping(True)
        screen.render_clipping(False)

        out, err = capfd.readouterr()
        assert out == ("page 1\n"
                       "vis iDischarge,0\n"
                       "b1label.txt=\"CLIPPING!\"\n"
                       "b1label.txt=\"\"\n")

    def test_it_closes_connection(self, screen, capfd):
        screen.close()
        out, err = capfd.readouterr()
        assert out == ("Connection closed\n")
