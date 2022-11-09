import webview
import os
import platform
import json

class Api:
    def __init__(self):
        self._window = None
        self.os = os.name
        self.platform = platform.system()
        self.release = platform.release()

    def set_window(self, window):
        self._window = window

    def window_close(self):
        self._window.destroy()

    def window_minimize(self):
        self._window.minimize()

    def get_system_info(self):
        return json.dumps({
            "platform": self.platform,
            "os":  self.os,
            "os_release": self.release
        })



if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Boilerplate App','./public/index.html', frameless=False, easy_drag=True, js_api=api)
    api.set_window(window)
    webview.start(debug=True)
