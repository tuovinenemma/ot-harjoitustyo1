import pygame

class Pacman:
    
    def __init__(self):
        #pelin alustuksia
        pygame.init()
        self.naytto = pygame.display.set_mode((840, 680)) 
        #ruma pacman en löytänyt parempaa tähän hätään :DD
        self.pacman = pygame.image.load("/home/emtuemtu/ot-harjoitustyo/laskarit/pacman/src/assets/pacman1.png")
        
        self.x = 0
        self.y = 680-self.pacman.get_height()
        
        
        self.oikealle = False
        self.vasemmalle = False
        self.ylos = False
        self.alas = False
        
    
        self.kello = pygame.time.Clock()
    
    
    def nayton_luominen(self): 
        
        self.naytto.fill((0, 0, 0))
        self.naytto.blit(self.pacman, (self.x, self.y))
        pygame.display.flip() 
        self.kello.tick(60)           
    

    #pacman liikkeet
    
    def handle_events(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle = True
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikealle = True
                if tapahtuma.key == pygame.K_UP:
                    self.ylos = True
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas = True

            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikealle = False
                if tapahtuma.key == pygame.K_UP:
                    self.ylos = False
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas = False
            if tapahtuma.type == pygame.QUIT:
                exit()
    
    
    def nappaimisto(self):            
        if self.ylos:
            if self.y >0:
                self.y -= 4
    
        if self.alas:
            if self.y < 680-self.pacman.get_height():
                self.y += 4
        
        if self.oikealle:
            if self.x <840-self.pacman.get_width():
                self.x += 4
        if self.vasemmalle:
            if self.x >0:
                self.x -= 4
                
        
    
    
    
#kutsutaan ohjelmaa

peli = Pacman()
while True:
    peli.handle_events()
    peli.nappaimisto()
    peli.nayton_luominen()
    
            

        
        
        
        
                
    
    
        
        