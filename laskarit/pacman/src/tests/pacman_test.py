import unittest
from peli import Pacman

class TestPacman(unittest.TestCase):
    def setUp(self):
        self.pacman = Pacman()

    def test_toimiiko_seina(self):
        self.pacman.vasemmalle = True
        for i in range(100):
            self.pacman.move_pacman()
            
        self.assertEqual(str(self.pacman.x), "0")
