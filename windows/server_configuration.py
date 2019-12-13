# Third party imports
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from windows.handlers.server_configuration import ServerConfigurationHandler


class ServerConfigurationWindow(Gtk.ApplicationWindow):
    """docstring for ServerConfiguration"""
    def __init__(self, app = None):
        super(ServerConfigurationWindow, self).__init__(title="Fruit Chaser", application=app)
        self.set_decorated(False)

        # Builder
        builder = Gtk.Builder()
        builder.add_from_file("windows/glade/server_configuration.glade")
        # Boxes
        box = builder.get_object("box")
        # Entrys
        self.nick = builder.get_object("nick")
        self.ip = builder.get_object("ip")
        self.port = builder.get_object("port")
        # Labels
        self.status = builder.get_object("status")

        # Handler
        handler = ServerConfigurationHandler(self)
        builder.connect_signals(handler)

        self.add(box)

        self.show_all()
        self.connect("destroy", handler.on_quit)
        handler.connect("play_signal", self.get_application().on_play_signal)


if __name__ == "__main__":
    ServerConfigurationWindow()
    Gtk.main()