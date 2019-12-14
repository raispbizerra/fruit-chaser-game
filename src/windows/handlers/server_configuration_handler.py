import gi

gi.require_version("Gtk", "3.0")
from gi.repository import GObject


class ServerConfigurationHandler(GObject.GObject):
    """docstring for ServerConfiguration"""

    def __init__(self, window):
        super(ServerConfigurationHandler, self).__init__()
        self.window = window
        self.nick = window.nick
        self.ip = window.ip
        self.port = window.port
        self.status = window.status

    def on_quit(self, button):
        """
        :param button:
        """
        self.window.get_application().quit()

    def on_play(self, button):
        # Clear status
        self.status.set_text("")

        # Get data
        nick, ip, port = self.nick.get_text(), self.ip.get_text(), self.port.get_text()

        # Check for empty data
        if not nick or not ip or not port:
            self.status.set_text("Fill data and try again.")
            return

        try:
            port = int(port)
        except ValueError:
            self.status.set_text("Incorrect data, try again.")
            return

        self.emit("play_signal", nick, ip, port)


GObject.type_register(ServerConfigurationHandler)
GObject.signal_new("play_signal", ServerConfigurationHandler, GObject.SIGNAL_ACTION,
                   GObject.TYPE_NONE, (str, str, int))
