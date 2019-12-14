# Third party imports
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from src.windows.handlers.server_configuration_handler import ServerConfigurationHandler


class ServerConfigurationWindow(Gtk.ApplicationWindow):
    """docstring for ServerConfiguration"""
    def __init__(self, app):
        # Init superclass
        super(ServerConfigurationWindow, self).__init__(title="Fruit Chaser", application=app)
        # Remove decoration
        self.set_decorated(False)
        # Set icon
        self.set_icon_from_file("src/windows/glade/media/icon.png")

        # Builder
        builder = Gtk.Builder()
        builder.add_from_file("src/windows/glade/server_configuration.glade")
        # Boxes
        box = builder.get_object("box")
        # Entries
        self.nick = builder.get_object("nick")
        self.ip = builder.get_object("ip")
        self.port = builder.get_object("port")
        # Labels
        self.status = builder.get_object("status")

        # Handler
        handler = ServerConfigurationHandler(self)
        builder.connect_signals(handler)

        # Add box to window
        self.add(box)

        # Connect signals
        self.connect("destroy", self.get_application().on_quit)
        handler.connect("play_signal", self.get_application().on_play_signal)


if __name__ == "__main__":
    ServerConfigurationWindow(None)
    Gtk.main()
