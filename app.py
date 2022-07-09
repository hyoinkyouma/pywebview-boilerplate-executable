import webview
import os

class Api:
    def __init__(self):
        self._window = None

    def set_window(self, window):
        self._window = window

    def windowClose(self):
        self._window.destroy()
    
    def windowMinimize(self):
        self._window.minimize()


if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Salarium', './public/index.html', frameless=True, easy_drag=True, js_api=api)
    api.set_window(window)
    webview.start()