import pygame
from pelinhallinta import Pelinhallinta
from peli import Pacman
from jono import Jono
def main():
    alusta = pygame.display.set_mode((1200, 1000))
    taso = Pacman(alusta)
    jono = Jono()
    peli = Pacman(alusta)
    pelinhallinta = Pelinhallinta(taso, alusta, jono, peli)
    pygame.init()
    pelinhallinta._aloita_peli()
if __name__ == "__main__":
    main()
    