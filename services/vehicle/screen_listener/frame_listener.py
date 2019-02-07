from services.vehicle.screen_renderers.settings_renderer import SettingsRenderer
from services.vehicle.screen_listener.screen_frame_processor import ScreenFrameProcessor

import threading
import time


class FrameListener:
    def __init__(self, communicator, frame_callback):
        self._communicator = communicator
        self._frame_callback = frame_callback
        self._settings_renderer = SettingsRenderer(communicator)
        self._screen_frame_processor = ScreenFrameProcessor()

    def start(self):
        self._settings_renderer.render()
        self._start_listener()

    def _start_listener(self):
        thread = threading.Thread(target=self._listen_screen)
        thread.start()

    def _listen_screen(self):
        while self._communicator.is_open():
            frame = self._communicator.readframe()
            if(len(frame) > 0):
                self._screen_frame_processor.process(frame, self._frame_callback)
                self._settings_renderer.render()

            time.sleep(0.1)
