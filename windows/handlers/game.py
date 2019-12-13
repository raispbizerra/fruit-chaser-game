import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GObject as gobject


class GameHandler(gobject.GObject):
    """docstring for ServerConfiguration"""
    def __init__(self, window):
        super(GameHandler, self).__init__()
        self.window = window

    def on_quit(self, button):
        print("quit")
        self.window.get_application().quit()

#         self.emit("play_signal", self.nick.get_text(), self.ip.get_text(), self.port.get_text())


# gobject.type_register(ServerConfigurationHandler)
# gobject.signal_new("play_signal", ServerConfigurationHandler, gobject.SIGNAL_ACTION,
#                gobject.TYPE_NONE, (str, str, str))