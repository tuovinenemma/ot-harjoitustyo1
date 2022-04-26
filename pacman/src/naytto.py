import pygame

class Naytto:
    def __init__(self,alusta,peli):
        self._alusta=alusta
        self._peli=peli
        
    def lataa(self):
        self._alusta.fill((0, 0, 0))
        self._alusta.blit(self._peli.pacman, (self._peli.x, self._peli.y))
        self._alusta.blit(self._peli.haamu, (self._peli.hx, self._peli.hy))
        pygame.display.flip()
        
        
    