from game import Game
from starting_screen import Start
import pygame 

def main():
    pygame.init()
    game = Game()
    game._game_running()
if __name__ == "__main__":
    main()
    