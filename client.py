#!venv/bin/python3
# -*- coding: utf-8 -*-
import sys
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from xmlrpc.client import ServerProxy
from src.windows.game_window import GameWindow
from src.windows.server_configuration_window import ServerConfigurationWindow


class Client(Gtk.Application):

    def do_activate(self):
        """
        Application activation
        :param self:
        :return: None
        """
        self._get_windows()
        self._add_windows()

    def _get_windows(self):
        """
        Application windows recover
        :return: None
        """
        self._server_configuration_window = ServerConfigurationWindow(self)
        self._game_window = GameWindow(self)

    def _add_windows(self):
        """
        Application windows addition
        @param self:
        @return: None
        """
        self.add_window(self._server_configuration_window)
        self.add_window(self._game_window)
        self._server_configuration_window.present()

    def on_play_signal(self, sender, nick, ip, port):
        """
        Play signal handler
        :param sender: Gtk.Widget
        :param nick: str
        :param ip: str
        :param port: str
        :return: None
        """
        self.nick = nick
        # Try connection
        try:
            self.server = ServerProxy(f"http://{ip}:{port}")
            self.id = self.server.connect(nick)
            self.game_state = self.server.get_state()
            self._server_configuration_window.hide()
            self._game_window.present()
        except Exception as e:
            sender.status.set_text(str(e))
            return

    def on_move(self, sender, move):
        """
        Move signal handler
        :param sender:
        :param move:
        :return: None
        """
        self.server.move_player(self.id, move)

    def on_get_state(self, sender):
        """
        Move signal handler
        :param sender:
        :return: None
        """
        self.game_state = self.server.get_state()

    def on_get_id(self, sender):
        """
        Get_id signal handler
        :param sender:
        :return: str
        """
        return self.id

    def on_get_nick(self, sender):
        """
        Get_nick signal handler
        :param sender:
        :return: str
        """
        return self.nick

    def on_quit(self, sender):
        """
        Quit signal handler
        :param sender:
        :return: None
        """
        self.server.quit(self.id)
        self.quit()


if __name__ == "__main__":
    app = Client()
    app.run(sys.argv)
