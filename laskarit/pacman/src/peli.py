import pygame
class Pacman:
    def __init__(self, alusta):
        pygame.init()
        self.alusta = alusta
        self.naytto = pygame.display.set_mode((1200, 1000))
        self.pacman = pygame.image.load(
            "/home/emtuemtu/ot-harjoitustyo/laskarit/pacman/src/assets/pacman1.png")
        self.haamu = pygame.image.load(
            "/home/emtuemtu/ot-harjoitustyo/laskarit/pacman/src/assets/haamu.png")
        self.x = 50 # pylint: disable=invalid-name
        self.y = 50 # pylint: disable=invalid-name
        self.hx = 100 # pylint: disable=invalid-name
        self.hy = 100 # pylint: disable=invalid-name
        self.nopeushx = 1
        self.nopeushy = 1
        self.oikealle = False
        self.vasemmalle = False
        self.ylos = False
        self.alas = False
        self.kello = pygame.time.Clock()     
    def update(self):
        self._move_ghost()
        self._move_pacman()
        self._lataanaytto()
    def _lataanaytto(self):
        self.alusta.fill((0, 0, 0))
        self.alusta.blit(self.pacman, (self.x, self.y))
        self.alusta.blit(self.haamu, (self.hx, self.hy))
        pygame.display.flip()
        self.kello.tick(60)
    def _move_pacman(self):
        if self.ylos:
            if self.y > 0:
                self.y -= 1
        if self.alas:
            if self.y < 1000-self.pacman.get_height():
                self.y += 1
        if self.oikealle:
            if self.x < 1200-self.pacman.get_width():
                self.x += 1
        if self.vasemmalle:
            if self.x > 0:
                self.x -= 1
    def _move_ghost(self):
        self.hx += self.nopeushx
        self.hy += self.nopeushy
        self.hy += self.nopeushy
        if self.nopeushy > 0 and self.hy+self.haamu.get_height() >= 1000:
            self.nopeushy = -self.nopeushy
        if self.nopeushy < 0 and self.hy <= 0:
            self.nopeushy = -self.nopeushy
        self.hx += self.nopeushx
        if self.nopeushx > 0 and self.hx+self.haamu.get_height() >= 1200:
            self.nopeushx = -self.nopeushx
        if self.nopeushx < 0 and self.hx <= 0:
            self.nopeushx = -self.nopeushx
            