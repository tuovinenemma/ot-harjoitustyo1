import pygame

class Start:
    def text1(self, words, screen, pos, size, colour, font_name, keskella=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if keskella:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)
        
    def text2(self):
        self.naytto.fill((0, 0, 0))
        self.tekstin_pohja('PUSH SPACE BAR TO START', self.naytto, [self.leveys//2, self.korkeus//2-50], 20, (170, 132, 58), 'arial black', keskella=True)
        self.tekstin_pohja('1 PLAYER ONLY', self.naytto, [self.leveys//2, self.korkeus//2+50], 20, (44, 167, 198), 'arial black', keskella=True)
        self.tekstin_pohja('PAC-MAN', self.naytto, [self.leveys//2, self.korkeus//2-150], 35, (255, 255, 0), 'arial black', keskella=True)
        self.tekstin_pohja('TOP SCORE:', self.naytto, [4, 0], 18, (255, 255, 255), 'arial black')