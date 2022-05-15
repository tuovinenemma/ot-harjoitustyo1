import pygame

class GameOver:
    def __init__(self, clock, events):
        pygame.init()
        self._clock = clock
        self._state = "game over"
        self._width = 700
        self._height = 875
        self._events = events
        self._screen = pygame.display.set_mode((self._width, self._height))
        
    def _end_text3(self, words, screen, pos, size, colour, font_name, middle=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if middle:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)
        
    def _end_text4(self):
        self._screen.fill((0, 0, 0))
        self._end_text3(f'SCORE: ', self._screen, [self._width//2, self._height//2-50], 30, (255, 255, 0), 'arial black', middle=True)
        self._end_text3('PUSH "R" TO RESTART', self._screen, [self._width//2, self._height//2+50], 30, (44, 167, 198), 'arial black', middle=True)
        self._end_text3('GAME OVER', self._screen, [self._width//2, self._height//2-150], 45, (255, 0, 0), 'arial black', middle=True)
        self._end_text3(f'HIGH SCORE: ', self._screen, [4, 0], 28, (0, 255, 0), 'arial black')
        
    def _end_game(self):
        self._end_text4()
        pygame.display.update()
        
    def _end_screen(self):
        self._end_game()
        while True:
            self._events._handle_events()
            if self._events._key_pressed == "restart":
                return
            self._render()
            pygame.display.update()
            self._clock.tick(60)
        
    def _game_ending(self):
        if self._state == "game over":
            self._ending()
            
    def _render(self):
        self._end_text4()