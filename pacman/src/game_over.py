import pygame
import sys
from game import Game

class GameOver:
    def __init__(self, clock, events):
        """lays the foundation for the end screen

        Args:
            clock
            events 
        """
        pygame.init()
        self._clock = clock
        self._state = "game over"
        self._width = 700
        self._height = 875
        self._events = events
        self._game = Game()
        self._screen = pygame.display.set_mode((self._width, self._height))
        
    def _end_text3(self, words, screen, pos, size, colour, font_name, middle=False):
        """lays the foundation for the end screen text

        Args:
            words 
            screen 
            pos 
            size 
            colour 
            font_name 
            middle - bool. Defaults to False.
        """
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if middle:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)
        
    def _end_text4(self):
        """creates the end screen text
        """
        self._screen.fill((0, 0, 0))
        self._end_text3(f'SCORE: ', self._screen, [self._width//2, self._height//2-50], 30, (255, 255, 0), 'arial black', middle=True)
        self._end_text3('PUSH "R" TO RESTART', self._screen, [self._width//2, self._height//2+50], 30, (44, 167, 198), 'arial black', middle=True)
        self._end_text3('PUSH "E" TO EXIT', self._screen, [self._width//2, self._height//2+100], 30, (44, 167, 198), 'arial black', middle=True)
        self._end_text3('GAME OVER', self._screen, [self._width//2, self._height//2-150], 45, (255, 0, 0), 'arial black', middle=True)
        self._end_text3(f'HIGH SCORE: {str(self._game._updateScore())}', self._screen, [4, 0], 28, (0, 255, 0), 'arial black')
        
    def _end_game(self):
        self._end_text4()
        pygame.display.update()
        
    def _end_screen(self):
        """checks the pressed key and takes it to restart or exit
        """
        self._end_game()
        while True:
            self._events._handle_events()
            if self._events._key_pressed == "restart":
                return
            if self._events._key_pressed == "exit":
                sys.exit()
            self._render()
            pygame.display.update()
            self._clock.tick(60)
        
    def _game_ending(self):
        if self._state == "game over":
            self._ending()
            
    def _render(self):
        self._end_text4()