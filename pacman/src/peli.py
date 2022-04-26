import pygame, sys
class Pacman:
    def __init__(self):
        pygame.init()
        
        #self.alusta = alusta
        self.state = 'start'
        self.running = True
        self.korkeus = 670
        self.leveys = 610
        self.naytto = pygame.display.set_mode((self.korkeus, self.leveys))
        self.kello = pygame.time.Clock()
        #self.pacman = pygame.image.load(
            #"/home/emtuemtu/ot-harjoitustyo/pacman/src/assets/pacman1.png")
        #self.haamu = pygame.image.load(
            #"/home/emtuemtu/ot-harjoitustyo/pacman/src/assets/haamu.png")
        #self.x = 50 # pylint: disable=invalid-name
        #self.y = 50 # pylint: disable=invalid-name
        #self.hx = 100 # pylint: disable=invalid-name
        #self.hy = 100 # pylint: disable=invalid-name
        #self.nopeushx = 1
        #self.nopeushy = 1
        #self.oikealle = False
        #self.vasemmalle = False
        #self.ylos = False
        #self.alas = False
        
             
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
        if self.nopeushy > 0 and self.hy+self.haamu.get_height() >= self.leveys:
            self.nopeushy = -self.nopeushy
        if self.nopeushy < 0 and self.hy <= 0:
            self.nopeushy = -self.nopeushy
        self.hx += self.nopeushx
        if self.nopeushx > 0 and self.hx+self.haamu.get_height() >= self.korkeus:
            self.nopeushx = -self.nopeushx
        if self.nopeushx < 0 and self.hx <= 0:
            self.nopeushx = -self.nopeushx
            
    def draw_text(self, words, screen, pos, size, colour, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)
            
    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw() 
            elif self.state == 'playing':
                self.playing_events()
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

    def start_draw(self):
        self.naytto.fill((0,0,0))
        self.draw_text('PUSH SPACE BAR TO START', self.naytto, [
                       self.leveys//2, self.korkeus//2-50], 16, (170, 132, 58), 'arial black', centered=True)
        self.draw_text('1 PLAYER ONLY', self.naytto, [
                       self.leveys//2, self.korkeus//2+50], 16, (44, 167, 198), 'arial black', centered=True)
        self.draw_text('HIGH SCORE:', self.naytto, [4, 0],
                       16, (255, 255, 255), 'arial black')
        pygame.display.update()
        
        
    def playing_events(self):
        for tapahtuma in self._jono.get():
            if tapahtuma.type == pygame.QUIT:
                self.running = False
            if tapahtuma.type == pygame.KEYDOWN:  # pylint: disable=no-member
                if tapahtuma.key == pygame.K_LEFT:  # pylint: disable=no-member
                    self._peli.vasemmalle = True
                if tapahtuma.key == pygame.K_RIGHT:  # pylint: disable=no-member
                    self._peli.oikealle = True
                if tapahtuma.key == pygame.K_UP:  # pylint: disable=no-member
                    self._peli.ylos = True
                if tapahtuma.key == pygame.K_DOWN:  # pylint: disable=no-member
                    self._peli.alas = True
            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_LEFT:  # pylint: disable=no-member
                    self._peli.vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:  # pylint: disable=no-member
                    self._peli.oikealle = False
                if tapahtuma.key == pygame.K_UP:  # pylint: disable=no-member
                    self._peli.ylos = False
                if tapahtuma.key == pygame.K_DOWN:  # pylint: disable=no-member
                    self._peli.alas = False
            