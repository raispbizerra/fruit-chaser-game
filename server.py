#!venv/bin/python3
# -*- coding: utf-8 -*-

import sys
from src import game as gm
from xmlrpc.server import SimpleXMLRPCServer

# Get IP and PORT to serve
try:
    IP = sys.argv[1]
    PORT = int(sys.argv[2])
except IndexError:
    IP = "localhost"
    PORT = 8000


class GameService:
    """This class represents a game service offered"""
    def __init__(self, game):
        # Number of players
        self.current_players = 0
        # Game
        self.game = game

    def connect(self, nick):
        """
        Handle player connection
        :param nick: str
        :return: str
        """
        # Increase player amount
        self.current_players += 1
        # Add player to the game
        self.game.add_player(str(self.current_players), nick)
        # Return player id
        return str(self.current_players)

    def get_state(self):
        """
        Get game state
        :return:
        """
        return self.game.state

    def quit(self, player_id):
        """
        Quit handler
        :param player_id:
        :return:
        """
        # Remove player
        self.game.rm_player(str(player_id))
        # Decrease player amount
        self.current_players -= 1
        return True

    def move_player(self, player_id, move):
        """
        Move player
        :param player_id:
        :param move:
        :return:
        """
        return self.game.move_player(player_id, move)


def main():
    """
    Main function
    """
    # Instantiate server
    with SimpleXMLRPCServer((IP, PORT)) as server:
        # Instantiate game
        game = gm.Game()
        # Register game instance allowing access to methods
        server.register_instance(GameService(game), allow_dotted_names=True)
        print(f'Serving XML-RPC on {IP} port {PORT}')
        # Start game
        game.start()
        try:
            # Serve
            server.serve_forever()
        except KeyboardInterrupt:
            # Stop game
            game.stop()
            print("\nKeyboard interrupt received, exiting.")
            sys.exit(0)


if __name__ == '__main__':
    main()
