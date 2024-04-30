import unittest
from game import TreasureMap, Player, Game

class TestTreasureMap(unittest.TestCase):
    def test_generate_treasure_location(self):
        map = TreasureMap()
        self.assertTrue(0 <= map.treasure_x < map.size)
        self.assertTrue(0 <= map.treasure_y < map.size)

    def test_check_treasure(self):
        map = TreasureMap()
        # Assuming the treasure is at (5, 5)
        map.treasure_x, map.treasure_y = 5, 5
        self.assertTrue(map.check_treasure(5, 5))
        self.assertFalse(map.check_treasure(5, 4))

    def test_get_hint(self):
        map = TreasureMap()
        map.treasure_x, map.treasure_y = 5, 5
        self.assertEqual(map.get_hint(5, 8), "Сокровище еще далеко.")
        self.assertEqual(map.get_hint(4, 5), "Вы близко к сокровищу!")

class TestPlayer(unittest.TestCase):
    def test_make_guess(self):
        player = Player()
        with unittest.mock.patch('builtins.input', return_value='5,5'):
            x, y = player.make_guess()
            self.assertEqual((x, y), (5, 5))

class TestGame(unittest.TestCase):
    def test_game_flow(self):
        game = Game()
        with unittest.mock.patch('builtins.input', return_value='5,5'), \
             unittest.mock.patch('builtins.print') as mocked_print:
            game.start()
            mocked_print.assert_called_with("Поздравляем! Вы нашли сокровище.")

if __name__ == '__main__':
    unittest.main()
