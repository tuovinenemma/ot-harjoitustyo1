import sys
import os
import pygame
from game_maze import *
from game_events import *
from sprites.player_pacman import Pacman
from sprites.player_ghost import Ghosts
dirname = os.path.dirname(__file__)
class Game:
    def __init__(self):
        pygame.init()
        self._clock = pygame.time.Clock()
        self._state = "game"
        self._screen = pygame.display.set_mode((700, 825))
        pygame.display.set_caption("Pacman")
        self._speed = 5
        self._maze = Maze(self._screen)
        self._key = "0"
        self._player = Pacman(self._speed)
        self._ghosts = Ghosts(self._speed)
        self._events = HandleEvents()

    def _start_game(self):
        self._maze._create_maze()
        self._screen.blit(self._player._pacman, (self._player.rect.x, self._player.rect.y))
        self._screen.blit(self._ghosts._ghosts, (self._ghosts.rect.x, self._ghosts.rect.y))
        pygame.display.update()
        
    def _render(self):
        self._maze._make_maze()
        self._move_pacman()
        self._screen.blit(self._player._pacman, (self._player.rect.x, self._player.rect.y))
        self._screen.blit(self._ghosts._ghosts, (self._ghosts.rect.x, self._ghosts.rect.y))

    def _move_pacman(self):
        key_pressed = self._events._key_pressed
        self._player._move(key_pressed)
        collision = pygame.sprite.spritecollide(self._player, self._maze._walls, False)
        if collision:
            self._player._move(key_pressed, collision=True)
            self._player._move(self._key)
            collision = pygame.sprite.spritecollide(self._player, self._maze._walls, False)
            if collision:
                self._player._move(self._key, collision=True)
                self._key = "0"
            return    
        self._key = key_pressed
        
    def _game_running(self):
        if self._state == "game":
            self._playing()
    
    def _playing(self):
        self._start_game()
        while True:
            self._events._handle_events()
            self._render()
            pygame.display.update()
            self._clock.tick(60)