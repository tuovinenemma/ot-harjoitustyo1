
import sys
import pygame
from sprites.player_pacman import Pacman

class GameEvents:
    """gets events
    """
    def get(self):
        return pygame.event.get()

class HandleEvents:
    """handles game events
    """
    def __init__(self):
        self._events = GameEvents()
        self._quit = False
        self._key_pressed = "0"
        
    def _handle_events(self):
        """definition for the keys

        Returns:
            what key is pressed
        """
        for event in self._events.get():
            if event.type == pygame.KEYDOWN:  # pylint: disable=no-member
                if event.key == pygame.K_LEFT:  # pylint: disable=no-member
                    self._key_pressed = "l"
                if event.key == pygame.K_RIGHT:  # pylint: disable=no-member
                    self._key_pressed = "r"
                if event.key == pygame.K_UP:  # pylint: disable=no-member
                    self._key_pressed = "u"
                if event.key == pygame.K_DOWN:  # pylint: disable=no-member
                    self._key_pressed = "d"
                if event.key == pygame.K_SPACE: # pylint: disable=no-member
                    self._key_pressed = "space"
                if event.key == pygame.K_q: # pylint: disable=no-member
                    self._key_pressed = "quit"
                if event.key == pygame.K_r: # pylint: disable=no-member
                    self._key_pressed = "restart"
                if event.key == pygame.K_e: # pylint: disable=no-member
                    self._key_pressed = "exit"
                
            if event.type == pygame.QUIT:  # pylint: disable=no-member
                sys.exit()
        
        return self._key_pressed