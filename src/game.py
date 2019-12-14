import inspect
import random
from src.timer import Timer

PLAYER_SIZE = 20
FIELD_SIZE = 500 - PLAYER_SIZE

POSITIONS = []
for x in range(0, FIELD_SIZE+PLAYER_SIZE, PLAYER_SIZE):
    for y in range(0, FIELD_SIZE+PLAYER_SIZE, PLAYER_SIZE):
        POSITIONS.append((x, y))


class Game:
    """docstring for Game"""

    def __init__(self):
        self.accepted_moves = {
            "UP": self._up,
            "DOWN": self._down,
            "LEFT": self._left,
            "RIGHT": self._right,
        }
        self._state = {'field_size': FIELD_SIZE, 'player_size': PLAYER_SIZE, 'players': {}, 'fruits': {}}
        self.fruit_timer = Timer(3, self.add_fruit)
        # self.collision_timer = Timer(3, self.add_fruit)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    def start(self):
        self.fruit_timer.start()

    def stop(self):
        self.fruit_timer.cancel()

    def add_player(self, player_id, nick):
        """
        Add player
        :param player_id:
        :param nick:
        :return: str
        """
        try:
            _ = self._state["players"][player_id]
            print("Fruit not added!")
            return f"Player {player_id} already exists!"
        except KeyError:
            x, y = random.choices(range(0, FIELD_SIZE+PLAYER_SIZE, PLAYER_SIZE), k=2)
            self._state["players"][player_id] = {"nick": nick, "x": x, "y": y, "p": 0}
            print("Fruit added!")
            return f"Player {player_id} added!"

    def rm_player(self, player_id):
        """
        Remove player
        :param player_id:
        :return: str
        """
        try:
            del self._state["players"][player_id]
            return f"Player {player_id} removed!"
        except KeyError:
            return f"Player {player_id} does not exist!"

    def field_is_full(self):
        """
        Check if field is full
        :return: bool
        """
        return len(self._state["fruits"]) >= ((FIELD_SIZE+PLAYER_SIZE) / PLAYER_SIZE) ** 2

    def add_fruit(self):
        """
        Add fruit
        :return: str
        """
        if self.field_is_full():
            return "Impossible to add fruit. Field is full!"

        positions = [x for x in POSITIONS if x not in self._state["fruits"].keys()]
        pos = random.choice(positions)
        self._state["fruits"][str(pos)] = True
        return "Fruit added!"

    def rm_fruit(self, pos):
        """
        Remove fruit
        :param pos:
        :return: str
        """
        try:
            del self._state["fruits"][str(pos)]
            return f"Fruit {pos} removed!"
        except KeyError:
            return f"Fruit {pos} does not exist!"

    def move_player(self, player_id, move):
        """
        Move player
        :param player_id:
        :param move:
        :return: str
        """
        try:
            self.accepted_moves[move](player_id)
            self.check_collision(player_id)
            return f"Player {player_id} moved {move}!"
        except KeyError:
            return "Invalid move!"

    def _up(self, player_id):
        try:
            self._state["players"][player_id]["y"] -= PLAYER_SIZE
            if self._state["players"][player_id]["y"] < 0:
                self._state["players"][player_id]["y"] = FIELD_SIZE
            return f"Player {player_id} moved {inspect.stack()[0][3]}!"
        except KeyError:
            return f"Player {player_id} does not exist!"

    def _down(self, player_id):
        try:
            self._state["players"][player_id]["y"] += PLAYER_SIZE
            if self._state["players"][player_id]["y"] > FIELD_SIZE:
                self._state["players"][player_id]["y"] = 0
            return f"Player {player_id} moved {inspect.stack()[0][3]}!"
        except KeyError:
            return f"Player {player_id} does not exist!"

    def _left(self, player_id):
        try:
            self._state["players"][player_id]["x"] -= PLAYER_SIZE
            if self._state["players"][player_id]["x"] < 0:
                self._state["players"][player_id]["x"] = FIELD_SIZE
            return f"Player {player_id} moved {inspect.stack()[0][3]}!"
        except KeyError:
            return f"Player {player_id} does not exist!"

    def _right(self, player_id):
        try:
            self._state["players"][player_id]["x"] += PLAYER_SIZE
            if self._state["players"][player_id]["x"] > FIELD_SIZE:
                self._state["players"][player_id]["x"] = 0
            return f"Player {player_id} moved {inspect.stack()[0][3]}!"
        except KeyError:
            return f"Player {player_id} does not exist!"

    def check_collision(self, player_id):
        player = self._state["players"][player_id]
        pos = player["x"], player["y"]
        try:
            _ = self._state["fruits"][str(pos)]
            player["p"] += 1
            self.rm_fruit(pos)
            return f"Player {player_id} collected a fruit at {pos}!"
        except KeyError:
            return f"There's no fruit at {pos}!"
