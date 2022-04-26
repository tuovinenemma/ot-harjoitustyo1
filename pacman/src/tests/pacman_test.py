import unittest
import pygame
from peli import Pacman


class TestPacman(unittest.TestCase):
    def setUp(self):
        self.pacman = Pacman()
        
    def test_toimiiko_seina(self):
        self.pacman.vasemmalle = True
        for i in range(100):
            self.pacman._move_pacman()
        self.assertEqual(str(self.pacman.x), "0")

    def test_toimiiko_haamun_liike_x(self):
        for i in range(300):
            self.pacman._move_ghost()
        self.assertNotEqual(str(self.pacman.hx), "100")
        
    def test_toimiiko_haamun_liike_y(self):
        for i in range(100):
            self.pacman._move_ghost()
        self.assertNotEqual(str(self.pacman.hy), "100")
        
    def test_toimiiko_aloitus_naytto(self):
        self.pacman.run()
        self.pacman.start_events()
        self.assertEqual(str(self.pacman.status), "playing")
        
        
  