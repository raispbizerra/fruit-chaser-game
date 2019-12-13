import unittest
import game as gm

class TestGame(unittest.TestCase):

    def test_player_op(self):
        game = gm.Game()

        ret = game.add_player(1)
        self.assertEqual(ret, "Player 1 added!")
        # print(ret, game.state["players"])

        ret = game.add_player(1)
        self.assertEqual(ret, "Player 1 already exists!")
        # print(ret, game.state["players"])

        ret = game.add_player(2)
        self.assertEqual(ret, "Player 2 added!")        
        # print(ret, game.state["players"])

        ret = game.rm_player(2)
        self.assertEqual(ret, "Player 2 removed!")        
        # print(ret, game.state["players"])

        ret = game.rm_player(2)
        self.assertEqual(ret, "Player 2 does not exist!")        
        # print(ret, game.state["players"])

        ret = game.move_player("UP", 1)
        self.assertEqual(ret, "Player 1 moved UP!")        
        # print(ret, game.state["players"])

        ret = game.move_player("DOWN", 1)
        self.assertEqual(ret, "Player 1 moved DOWN!")        
        # print(ret, game.state["players"])

        ret = game.move_player("LEFT", 1)
        self.assertEqual(ret, "Player 1 moved LEFT!")        
        # print(ret, game.state["players"])

        ret = game.move_player("RIGHT", 1)
        self.assertEqual(ret, "Player 1 moved RIGHT!")        
        # print(ret, game.state["players"])

        ret = game.move_player("UPPER", 1)
        self.assertEqual(ret, "Invalid move!")
        # print(ret, game.state["players"])

        ret = game.move_player("UP", 2)
        self.assertEqual(ret, "Invalid move!")
        # print(ret, game.state["players"])

        game.state["players"][1] = {"x": 0, "y": 0, "p": 0}

        ret = game.move_player("UP", 1)
        self.assertEqual(ret, "Player 1 moved UP!")        
        # print(ret, game.state["players"])        

        ret = game.move_player("LEFT", 1)
        self.assertEqual(ret, "Player 1 moved LEFT!")        
        # print(ret, game.state["players"])

        ret = game.move_player("DOWN", 1)
        self.assertEqual(ret, "Player 1 moved DOWN!")        
        # print(ret, game.state["players"])

        ret = game.move_player("RIGHT", 1)
        self.assertEqual(ret, "Player 1 moved RIGHT!")        
        # print(ret, game.state["players"])

        del game

    def test_fruit_op(self):
        game = gm.Game()

        for _ in range(625):
            ret = game.add_fruit()
            self.assertEqual(ret, "Fruit added!")

        ret = game.add_fruit()
        self.assertEqual(ret, "Impossible to add fruit. Field is full!")

        ret = game.rm_fruit((0, 0))
        self.assertEqual(ret, "Fruit (0, 0) removed!")

        ret = game.rm_fruit((0, 0))
        self.assertEqual(ret, "Fruit (0, 0) does not exist!")

        ret = game.add_fruit()
        self.assertEqual(ret, "Fruit added!")

        ret = game.add_fruit()
        self.assertEqual(ret, "Impossible to add fruit. Field is full!")

        for pos in gm.POSITIONS:
            ret = game.rm_fruit(pos)
            self.assertEqual(ret, f"Fruit {pos} removed!")

        ret = game.rm_fruit((0, 0))
        self.assertEqual(ret, "Fruit (0, 0) does not exist!")

        del game

    def test_collision(self):
        game = gm.Game()

        ret = game.add_fruit()
        self.assertEqual(ret, "Fruit added!")

        ret = game.add_player(1)
        self.assertEqual(ret, "Player 1 added!")
        x, y = list(game.state["fruits"].keys())[0]
        game.state["players"][1] = {"x": x, "y": y, "p": 0}

        player_id = 1
        player = game.state["players"][player_id]
        pos = player["x"], player["y"]
        ret = game.check_collision(player_id)
        self.assertEqual(ret, f"Player {player_id} collected a fruit at {pos}!")

        player_id = 1
        player = game.state["players"][player_id]
        pos = player["x"], player["y"]
        ret = game.check_collision(player_id)
        self.assertEqual(ret, f"There's no fruit at {pos}!")

        del game

if __name__ == "__main__":
    unittest.main()