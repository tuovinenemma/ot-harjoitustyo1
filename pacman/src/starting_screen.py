import pygame
from game_events import *

class Start:
    def __init__(self, events, clock):
        """lays the foundation for the start screen

        Args:
            events 
            clock = fps int
        """
        pygame.init()
        self._clock = clock
        self._state = "start"
        self._width = 700
        self._height = 875
        self._events = events
        self._screen = pygame.display.set_mode((self._width, self._height))
        
    def _start_text1(self, words, screen, pos, size, colour, font_name, middle=False):
        """lays the foundation for the start screen text

        Args:
            words = str
            screen 
            pos = x,y
            size = int
            colour = rgb
            font_name = str
            middle - bool, Defaults to False.
        """
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if middle:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)
        
    def _start_text2(self, highscore):
        """creates the text for start screen
        """
        pygame.mouse.set_visible(0)
        self._screen.fill((0, 0, 0))
        self._start_text1('PUSH SPACE BAR TO START', self._screen, [self._width//2, self._height//2-40], 30, (170, 132, 58), 'arial black', middle=True)
        self._start_text1('1 PLAYER ONLY', self._screen, [self._width//2, self._height//2+50], 30, (44, 167, 198), 'arial black', middle=True)
        self._start_text1('PAC-MAN', self._screen, [self._width//2, self._height//2-150], 45, (255, 255, 0), 'arial black', middle=True)
        
        
    def _start_game(self, highscore):
        """starts the start screen
        """
        self._start_text2(highscore)
        pygame.display.update()
        
    def _start_screen(self, highscore):
        """starts and checks the key pressed
        """
        self._start_game(highscore)
        while True:
            self._events._handle_events()
            if self._events._key_pressed == "space":
                return
            self._render(highscore)
            pygame.display.update()
            self._clock.tick(60)
        
    def _game_starting(self):
        """checks status and acts
        """
        if self._state == "start":
            self._starting()
            
    def _render(self,highscore):
        """renders
        """
        self._start_text2(highscore)