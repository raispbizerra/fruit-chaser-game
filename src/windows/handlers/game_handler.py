import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, Gdk, GObject
DT = 50


class GameHandler(GObject.GObject):
    """docstring for ServerConfiguration"""
    def __init__(self, window):
        super(GameHandler, self).__init__()
        self.window = window
        self.drawing_area = window.drawing_area
        self.liststore = window.liststore

    def on_show(self, window):
        self.id = self.emit("get_id")
        self.nick = self.emit("get_nick")
        self.state = self.window.get_application().game_state
        GLib.timeout_add(DT, self.update_screen)

    def update_screen(self):
        self.emit("get_state")
        self.state = self.window.get_application().game_state
        self.fill_liststore()
        self.drawing_area.queue_draw()
        return True

    def fill_liststore(self):
        self.liststore.clear()

        for key, dic in self.state["players"].items():
            data = [dic["nick"], dic["p"], key]
            self.liststore.append(data)

        self.liststore.set_sort_column_id(1, Gtk.SortType.DESCENDING)

    def on_draw(self, widget, cr):
        cr.set_source_rgb(1, 1, 1)
        cr.paint()

        for _, dic in self.state["players"].items():
            cr.set_source_rgb(.8,.8,.8)
            cr.rectangle(dic["x"], dic["y"],self.state["player_size"],self.state["player_size"])
            cr.fill()

        for pos, _ in self.state["fruits"].items():
            pos = [int(x) for x in pos[1:-1].split(',')]
            cr.set_source_rgb(0,1,0)
            cr.rectangle(pos[0], pos[1],self.state["player_size"],self.state["player_size"])
            cr.fill()

        cr.set_source_rgb(0, 0, 0)
        x, y = self.state["players"][self.id]["x"], self.state["players"][self.id]["y"]
        cr.rectangle(x, y,self.state["player_size"],self.state["player_size"])
        cr.fill()

    def on_key_press_event(self, widget, event):
        key = Gdk.keyval_name(event.keyval).upper()
        if key == "ESCAPE":
            self.window.get_application().on_quit(self.window)
        else:
            self.emit("move", key)

GObject.type_register(GameHandler)
GObject.signal_new("get_state", GameHandler, GObject.SIGNAL_ACTION, None, ())
GObject.signal_new("get_id", GameHandler, GObject.SIGNAL_ACTION, str, ())
GObject.signal_new("get_nick", GameHandler, GObject.SIGNAL_ACTION, str, ())
GObject.signal_new("move", GameHandler, GObject.SIGNAL_ACTION, None, (str,))