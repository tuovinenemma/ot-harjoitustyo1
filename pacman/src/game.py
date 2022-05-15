import sys
import os
import pygame
from game_maze import *
from game_events import *
from game_over import GameOver
from sprites.player_pacman import Pacman
from sprites.player_ghost import Ghosts
from starting_screen import Start
from game_over import GameOver
dirname = os.path.dirname(__file__)
class Game:
    def __init__(self):
        pygame.init()
        self._clock = pygame.time.Clock()
        self._state = "start"
        self._width = 700
        self._height = 875
        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption("Pacman")
        self._speed = 5
        self._maze = Maze(self._screen)
        self._key = "0"
        self._count = 0
        self._lives = 3
        self._high_score = 0
        self._player = Pacman(self._speed)
        self._ghosts = Ghosts(self._speed)
        self._events = HandleEvents()
        self._start = Start(self._events, self._clock)
        self._end = GameOver(self._clock, self._events)

    def _start_game(self):
        self._maze._create_maze()
        self._screen.blit(self._player._pacman, (self._player.rect.x, self._player.rect.y))
        self._screen.blit(self._ghosts._ghosts, (self._ghosts.rect.x, self._ghosts.rect.y))
        self._game_text2()
        pygame.display.update()

        
    def _render(self):
        self._maze._make_maze()
        self._move_pacman()
        self._eat_largepellet()
        self._eat_pellet()
        self._eat_cherries()
        self._eat_strawberries()
        #self._hit_ghost()
        self._screen.blit(self._player._pacman, (self._player.rect.x, self._player.rect.y))
        self._screen.blit(self._ghosts._ghosts, (self._ghosts.rect.x, self._ghosts.rect.y))
        self._game_text2()

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
        
        if self._player.rect.x < 0:
            self._player.rect.x = 700
            self._screen.blit(self._player._pacman, (self._player.rect.x, self._player.rect.y))
            
        elif self._player.rect.x > 700:
            self._player.rect.x = 0
            self._screen.blit(self._player._pacman, (self._player.rect.x, self._player.rect.y))

        
    def _game_running(self):
        while True:
            if self._state == "start":
                self._start._start_screen()
                self._state = "game"
            if self._state == "game":
                self._playing()
                self._state = "game over"
            if self._state == "game over":
                self._end._end_screen()
                self._state = "start"
  
    
    def _playing(self):
        self._start_game()
        while True:
            self._events._handle_events()
            if self._events._key_pressed == "quit":
                return
            self._render()
            pygame.display.update()
            self._clock.tick(60)
            
    def _game_text(self, words, screen, pos, size, colour, font_name):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        screen.blit(text, pos)
        
    def _game_text2(self):
        self._game_text(f'SCORE: {self._count}', self._screen, [4, 0], 25, (255, 255, 255), 'arial black')
        self._game_text(f'HIGH SCORE: {self._high_score}', self._screen, [450, 0], 25, (255, 255, 255), 'arial black')
        self._game_text(f'LIVES: {self._lives}', self._screen, [4, 830], 25, (255, 255, 255), 'arial black')
        self._game_text(f'press "q" to quit', self._screen, [450, 830], 25, (255, 255, 255), 'arial black')

        
    def _eat_pellet(self):
        eat = pygame.sprite.spritecollide(self._player, self._maze._pellet, True)
        for pellet in eat:
            self._count += 1
            self._maze._pellet.remove(pellet)
            
            
    def _eat_largepellet(self):
        eatlarge = pygame.sprite.spritecollide(self._player, self._maze._largepellet, True)
        for largepellet in eatlarge:
            self._count += 100
            self._maze._largepellet.remove(largepellet)
            
    def _eat_cherries(self):
        eatcherries = pygame.sprite.spritecollide(self._player, self._maze._cherry, True)
        for cherry in eatcherries:
            self._count += 50
            self._maze._largepellet.remove(cherry)
            
    def _eat_strawberries(self):
        eatstrawberries = pygame.sprite.spritecollide(self._player, self._maze._strawberry, True)
        for strawberry in eatstrawberries:
            self._count += 200
            self._maze._largepellet.remove(strawberry)
            
    def _hit_ghost(self):
        hit = pygame.sprite.spritecollide(self._player, self._ghosts, True)
        for ghost in hit:
            self._lives -= 1
        