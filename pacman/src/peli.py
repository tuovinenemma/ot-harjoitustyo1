import sys
import pygame
from pelinhallinta import Pelinhallinta
from jono import Jono
class Pacman:
    def __init__(self):
        pygame.init()
        self.state = 'start game'
        self.running = True
        self.korkeus = 500
        self.leveys = 500
        self.naytto = pygame.display.set_mode((self.korkeus, self.leveys))
        self.kello = pygame.time.Clock()
        self.pacman = pygame.image.load("/home/emtuemtu/ot-harjoitustyo/pacman/src/assets/pacman1.png")
        self.pacman = pygame.transform.scale(self.pacman, (100, 100))
        self.haamu = pygame.image.load("/home/emtuemtu/ot-harjoitustyo/pacman/src/assets/haamu.png")
        self.haamu = pygame.transform.scale(self.haamu, (100, 100))
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
    def update(self):
        self._move_ghost()
        self._move_pacman()
        self._lataanaytto()
    def _lataanaytto(self):
        self.naytto.fill((0, 0, 0))
        self.naytto.blit(self.pacman, (self.x, self.y))
        self.naytto.blit(self.haamu, (self.hx, self.hy))
        pygame.display.flip()
        self.kello.tick(60)
    def _move_pacman(self):
        if self.ylos:
            if self.y > 0:
                self.y -= 1
        if self.alas:
            if self.y < self.leveys-self.pacman.get_height():
                self.y += 1
        if self.oikealle:
            if self.x < self.korkeus-self.pacman.get_width():
                self.x += 1
        if self.vasemmalle:
            if self.x > 0:
                self.x -= 1
    def _move_ghost(self):
        self.hx += self.nopeushx
        self.hy += self.nopeushy
        self.hy += self.nopeushy
        if self.nopeushy > 0 and self.hy+self.haamu.get_height() >= self.leveys:
            self.nopeushy = -self.nopeushy
        if self.nopeushy < 0 and self.hy <= 0:
            self.nopeushy = -self.nopeushy
        self.hx += self.nopeushx
        if self.nopeushx > 0 and self.hx+self.haamu.get_height() >= self.korkeus:
            self.nopeushx = -self.nopeushx
        if self.nopeushx < 0 and self.hx <= 0:
            self.nopeushx = -self.nopeushx
    def tekstin_pohja(self, words, screen, pos, size, colour, font_name, keskella=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if keskella:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)
    def run(self):
        while self.running:
            if self.state == 'start game':
                self.start_events()
                self.start_update()
                self.teksti()
            elif self.state == 'playing':
                self.start_playing()
            else:
                self.running = False
            self.kello.tick(60)
        pygame.quit()
        sys.exit()
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'
    def start_update(self):
        pass
    def teksti(self):
        self.naytto.fill((0, 0, 0))
        self.tekstin_pohja('PUSH SPACE BAR TO START', self.naytto, [self.leveys//2, self.korkeus//2-50], 20, (170, 132, 58), 'arial black', keskella=True)
        self.tekstin_pohja('1 PLAYER ONLY', self.naytto, [self.leveys//2, self.korkeus//2+50], 20, (44, 167, 198), 'arial black', keskella=True)
        self.tekstin_pohja('PAC-MAN', self.naytto, [self.leveys//2, self.korkeus//2-150], 35, (255, 255, 0), 'arial black', keskella=True)
        self.tekstin_pohja('TOP SCORE:', self.naytto, [4, 0], 18, (255, 255, 255), 'arial black')
        pygame.display.update()
    def start_playing(self):
        taso = Pacman()
        jono = Jono()
        pelinhallinta = Pelinhallinta(taso, self.naytto, jono)
        pygame.init()
        pelinhallinta.aloita_peli()
            