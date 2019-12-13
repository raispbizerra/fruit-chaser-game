#!venv/bin/python3
# -*- coding: utf-8 -*-

import sys
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from xmlrpc.client import ServerProxy, MultiCall

from windows.server_configuration import ServerConfigurationWindow
from windows.game import GameWindow
from signals import Receiver

class Client(Gtk.Application):
    def do_activate(self):
        self._get_windows()
        self._add_windows()

    def _get_windows(self):
        self._server_configuration = ServerConfigurationWindow(self)
        self._game = GameWindow(self)
    
    def _add_windows(self):
        self.add_window(self._server_configuration)
        self.add_window(self._game)
        self._server_configuration.present()

    def on_play_signal(self, sender, nick, ip, port):
        # Try connection
        try:
            try:
                port = int(port)
                self.server = ServerProxy(f"http://{ip}:{port}")
                # try:
                #     dt = server.CurrentTime.get_current_time()
                # except Exception as e:
                #     sender.status.set_text(str(e))
                #     print("ERROR", e)
                #     return

                # multi = MultiCall(server)
                self.client_id = self.server.get_id()
                print(self.client_id)
                self._server_configuration.hide()
                self._game.present()
                # multi.get_game_state(2,9)
                # multi.add(1,2)
                # try:
                #     for response in multi():
                #         print(response)
                # except Exception as e:
                #     sender.status.set_text(str(e))
                #     print("ERROR", e)
                #     return
            except ValueError as e:
                sender.status.set_text("Incorrect data, try again.")
                print(e)
                return
        except Exception as e:
            sender.status.set_text(str(e))
            print("ERROR", e)
            return

    def on_quit(self):
        self.server.quit()


if __name__ == "__main__":
    app = Client()
    app.run(sys.argv)