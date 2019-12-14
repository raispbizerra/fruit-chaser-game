# Third party imports
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from src.windows.handlers.game_handler import GameHandler


class GameWindow(Gtk.ApplicationWindow):
    """docstring for ServerConfiguration"""
    def __init__(self, app):
        # Init superclass
        super(GameWindow, self).__init__(title="Fruit Chaser", application=app)
        # Remove decoration
        self.set_decorated(False)
        #Set icon
        self.set_icon_from_file("src/windows/glade/media/icon.png")

        # Builder
        builder = Gtk.Builder()
        builder.add_from_file("src/windows/glade/game.glade")
        # Boxes
        box = builder.get_object("box")
        # Drawing Area (canvas)
        self.drawing_area = builder.get_object("drawing_area")
        self.liststore = builder.get_object("liststore")

        # Handler
        handler = GameHandler(self)
        builder.connect_signals(handler)

        # Add box
        self.add(box)

        # Set fullscreen
        self.fullscreen()

        # Connect signals
        self.connect("show", handler.on_show)
        self.connect("destroy", self.get_application().on_quit)
        self.connect("key-press-event", handler.on_key_press_event)
        handler.connect("get_state", self.get_application().on_get_state)
        handler.connect("get_id", self.get_application().on_get_id)
        handler.connect("get_nick", self.get_application().on_get_nick)
        handler.connect("move", self.get_application().on_move)


if __name__ == "__main__":
    g = GameWindow(None)
    g.show_all()
    Gtk.main()
