import unittest
import randomgame


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = randomgame.thegame()
        self.assertEqual(result, 15)


unittest.main()
