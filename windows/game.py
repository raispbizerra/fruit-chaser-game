# Third party imports
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from windows.handlers.game import GameHandler


class GameWindow(Gtk.ApplicationWindow):
    """docstring for ServerConfiguration"""
    def __init__(self, app = None):
        super(GameWindow, self).__init__(title="Fruit Chaser", application=app)
        self.set_decorated(False)

        # Builder
        builder = Gtk.Builder()
        builder.add_from_file("windows/glade/game.glade")
        # Boxes
        box = builder.get_object("box")

        # Handler
        handler = GameHandler(self)
        builder.connect_signals(handler)

        self.add(box)

        # self.show_all()
        self.fullscreen()
        self.connect("destroy", handler.on_quit)
        # handler.connect("play_signal", self.get_application().on_play_signal)


if __name__ == "__main__":
    GameWindow()
    Gtk.main()