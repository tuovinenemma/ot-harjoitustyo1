import pygame

class Pelinhallinta:
    def __init__(self, taso, alusta, jono, peli):
        self._peli = peli
        self._taso = taso
        self._alusta = alusta
        self._jono = jono
        
    def _aloita_peli(self):
        while True:
            self._handle_events()
            self._peli.update()
            
            
    def _handle_events(self):
        for tapahtuma in self._jono.get():
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
            if tapahtuma.type == pygame.QUIT:  # pylint: disable=no-member
                exit()