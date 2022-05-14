import pygame
import os
dirname = os.path.dirname(__file__)

class Ghosts(pygame.sprite.Sprite):

    def __init__(self, speed):
        self._ghosts = pygame.image.load(os.path.join(dirname, "..", "assets", "ghost.png"))
        self._ghosts = pygame.transform.smoothscale(self._ghosts, (30, 30))
        self._speed = speed
        self.rect = self._ghosts.get_rect()
        self.rect.x = 325
        self.rect.y = 410
