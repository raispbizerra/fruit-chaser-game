from random import choice, choices
from inspect import stack

PLAYER_SIZE = 20
FIELD_SIZE = 500 - PLAYER_SIZE

POSITIONS = []
for x in range(0, FIELD_SIZE+PLAYER_SIZE, PLAYER_SIZE):
    for y in range(0, FIELD_SIZE+PLAYER_SIZE, PLAYER_SIZE):
        POSITIONS.append((x, y))


class Game:
    """docstring for Game"""
    def __init__(self):
        self._state = {
            "players": {},
            "fruits": {}
        }

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    
    def add_player(self, player_id):
        try:
            _ = self._state["players"][player_id]
            return f"Player {player_id} already exists!"
        except:
            x, y = choices(range(0, FIELD_SIZE+PLAYER_SIZE, PLAYER_SIZE), k=2)
            self._state["players"][player_id] = {"x": x, "y": y, "p": 0}
            return f"Player {player_id} added!"

    def rm_player(self, player_id):
        try:
            del self._state["players"][player_id]
            return f"Player {player_id} removed!"
        except:
            return f"Player {player_id} does not exist!"

    def field_is_full(self):
        return len(self._state["fruits"]) >= ((FIELD_SIZE+PLAYER_SIZE) / PLAYER_SIZE) ** 2

    def add_fruit(self):
        if self.field_is_full():
            return "Impossible to add fruit. Field is full!"
        
        positions = [x for x in POSITIONS if x not in self._state["fruits"].keys()]
        pos = choice(positions)
        self._state["fruits"][pos] = True
        return f"Fruit added!"

    def rm_fruit(self, pos):
        try:
            del self._state["fruits"][pos]
            return f"Fruit {pos} removed!"
        except:
            return f"Fruit {pos} does not exist!"

    def move_player(self, move, player_id):
        accepted_moves = {
            "UP": self._up,
            "DOWN": self._down,
            "LEFT": self._left,
            "RIGHT": self._right,
            "ESCAPE": self.rm_player
        }

        try:
            accepted_moves[move](player_id)
            return f"Player {player_id} moved {move}!"
            # self.check_collision(player_id)
        # except Exception as e:
            # return "Invalid move!", e
        except:
            return "Invalid move!"

    def _up(self, player_id):
        try:
            self._state["players"][player_id]["y"] -= PLAYER_SIZE
            if self._state["players"][player_id]["y"] <= 0:
                self._state["players"][player_id]["y"] = FIELD_SIZE
            return f"Player {player_id} moved {stack()[0][3]}!"
        except Exception as e:
            raise e
            return f"Player {player_id} does not exist!"
    
    def _down(self, player_id):
        try:
            self._state["players"][player_id]["y"] += PLAYER_SIZE
            if self._state["players"][player_id]["y"] > FIELD_SIZE:
                self._state["players"][player_id]["y"] = 0
            return f"Player {player_id} moved {stack()[0][3]}!"
        except Exception as e:
            # raise e
            return f"Player {player_id} does not exist!"
    
    def _left(self, player_id):
        try:
            self._state["players"][player_id]["x"] -= PLAYER_SIZE
            if self._state["players"][player_id]["x"] <= 0:
                self._state["players"][player_id]["x"] = FIELD_SIZE
            return f"Player {player_id} moved {stack()[0][3]}!"
        except Exception as e:
            raise e
            return f"Player {player_id} does not exist!"
    
    def _right(self, player_id):
        try:
            self._state["players"][player_id]["x"] += PLAYER_SIZE
            if self._state["players"][player_id]["x"] > FIELD_SIZE:
                self._state["players"][player_id]["x"] = 0
            return f"Player {player_id} moved {stack()[0][3]}!"
        except Exception as e:
            # raise e
            return f"Player {player_id} does not exist!"

    def check_collision(self, player_id):
        player = self._state["players"][player_id]
        pos = player["x"], player["y"]
        try:
            _ = self._state["fruits"][pos]
            player["p"] += 1
            self.rm_fruit(pos)
            return f"Player {player_id} collected a fruit at {pos}!"
        except:
            return f"There's no fruit at {pos}!"
