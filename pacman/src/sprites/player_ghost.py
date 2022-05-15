import pygame
import os
from random import randint
dirname = os.path.dirname(__file__)

class Ghosts(pygame.sprite.Sprite):

    def __init__(self, speed):
        super().__init__()
        """lays tthe foundation for ghosts
        Args:
            speed = int
        """
        self._ghost = pygame.image.load(os.path.join(dirname, "..", "assets", "ghost.png"))
        self._ghost = pygame.transform.smoothscale(self._ghost, (25, 25))
        self._speed = 2
        self.rect = self._ghost.get_rect()
        self.rect.x = 325
        self.rect.y = 410
        self._ghost_direction = 3
        

        