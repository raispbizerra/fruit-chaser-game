#!venv/bin/python3
# -*- coding: utf-8 -*-

import sys
import datetime
import game as gm
from xmlrpc.server import SimpleXMLRPCServer

try:
    IP = sys.argv[1]
    PORT = int(sys.argv[2])
except IndexError:
    IP = "localhost"
    PORT = 8000


class GameService:
    def __init__(self, game):
        self.current_players = 0
        self.game = game

    def get_id(self):
        self.current_players += 1
        self.game.add_player(self.current_players)
        return self.current_players

    def quit(self, player_id):
        self.game.rm_player(player_id)
        self.current_players -= 1
        return True

    def getData(self):
        return '42'

    class CurrentTime:
        @staticmethod
        def get_current_time():
            return datetime.datetime.now()


with SimpleXMLRPCServer((IP, PORT)) as server:
    game = gm.Game()
    # server.register_function(pow)
    # server.register_function(lambda x,y: x+y, 'add')
    server.register_instance(GameService(game), allow_dotted_names=True)
    server.register_multicall_functions()
    print(f'Serving XML-RPC on {IP} port {PORT}')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        sys.exit(0)