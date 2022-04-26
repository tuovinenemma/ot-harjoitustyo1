import unittest
import pygame
from peli import Pacman


class TestPacman(unittest.TestCase):
    def setUp(self):
        self.pacman = Pacman()
        
    def test_toimiiko_seina_vasen(self):
        self.pacman.vasemmalle = True
        for i in range(100):
            self.pacman._move_pacman()
        self.assertEqual(str(self.pacman.x), "0")
        
    def test_toimiiko_seina_oikea(self):
        self.pacman.oikealle = True
        for i in range(10000):
            self.pacman._move_pacman()
        self.assertEqual((self.pacman.x), self.pacman.leveys-100)

    def test_toimiiko_seina_ala(self):
        self.pacman.alas = True
        for i in range(10000):
            self.pacman._move_pacman()
        self.assertEqual((self.pacman.y), self.pacman.korkeus-100)
        
    def test_toimiiko_seina_yla(self):
        self.pacman.ylos = True
        for i in range(10000):
            self.pacman._move_pacman()
        self.assertEqual((self.pacman.y), 0)
        
    def test_toimiiko_haamun_liike_x(self):
        for i in range(5):
            self.pacman._move_ghost()
        self.assertNotEqual(str(self.pacman.hx), "100")
        
    def test_toimiiko_haamun_liike_y(self):
        for i in range(100):
            self.pacman._move_ghost()
        self.assertNotEqual(str(self.pacman.hy), "100")
        
    def test_asetetaan_state(self):
        self.pacman._state = "start game"
        
    def test_pacmanin_liike_oikea(self):
        self.pacman.x = 0
        self.pacman.oikealle = True
        self.pacman._move_pacman()
        self.assertGreater((self.pacman.x), 0)
        
    def test_pacmanin_liike_vasen(self):
        self.pacman.x = 200
        self.pacman.vasemmalle = True
        self.pacman._move_pacman()
        self.assertLess((self.pacman.x), 200)

    def test_pacmanin_liike_ylos(self):
        self.pacman.y = 200
        self.pacman.ylos = True
        self.pacman._move_pacman()
        self.assertLess((self.pacman.y), 200)

    def test_pacmanin_liike_alas(self):
        self.pacman.y = 200
        self.pacman.alas = True
        self.pacman._move_pacman()
        self.assertGreater((self.pacman.y), 200)
        
  