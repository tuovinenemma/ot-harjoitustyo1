import pygame
import os

dirname = os.path.dirname(__file__)

class Pacman(pygame.sprite.Sprite):

    def __init__(self, speed, image=None):
        """lays the foundation for player pacman

        Args:
            speed = int
            image = png
        """
        self._pacman = pygame.image.load(os.path.join(dirname, "..", "assets", "pacman.png"))
        self._pacman = pygame.transform.smoothscale(self._pacman, (25, 25))
        self._speed = speed
        self.rect = self._pacman.get_rect()
        self.rect.x = 323
        self.rect.y = 625

    def _move(self, key_pressed, collision=None):
        """movement for pacman

        Args:
            what key is pressed
            is there collision 
        """
        if collision:
            if key_pressed == "l":
                self.rect.x += self._speed
            if key_pressed == "r":
                self.rect.x -= self._speed
            if key_pressed == "u":
                self.rect.y += self._speed
            if key_pressed == "d":
                self.rect.y -= self._speed
        else:
            if key_pressed == "l":
                self.rect.x -= self._speed
            if key_pressed == "r":
                self.rect.x += self._speed
            if key_pressed == "u":
                self.rect.y -= self._speed
            if key_pressed == "d":
                self.rect.y += self._speed
            