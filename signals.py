import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GObject as gobject
from gi.repository import Gtk


class Sender(gobject.GObject):
    def __init__(self):
        super(Sender, self).__init__()
        # self.__gobject_init__()

gobject.type_register(Sender)
gobject.signal_new("play_signal", Sender, gobject.SIGNAL_ACTION,
                   gobject.TYPE_NONE, ())


class Receiver(Gtk.Window):
    def __init__(self, sender):
        super(Receiver, self).__init__()
        # self.__gobject_init__()
        
        sender.connect('play_signal', self.on_play_signal)
        
    def on_play_signal(self, sender):
        print ("Receiver reacts to play_signal")


def user_callback(object):
    print ("user callback reacts to play_signal")

if __name__ == '__main__':
    
    sender = Sender()
    receiver = Receiver(sender)

    # sender.connect("play_signal", user_callback)
    sender.emit("play_signal")