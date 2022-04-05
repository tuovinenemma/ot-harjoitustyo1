import pygame

class Pacman:
    
    def __init__(self):
        #pelin alustuksia
        pygame.init()
        self.naytto = pygame.display.set_mode((1000, 1000)) 
        #ruma pacman en löytänyt parempaa tähän hätään :DD
        self.pacman = pygame.image.load("/home/emtuemtu/ot-harjoitustyo/laskarit/pacman/src/assets/pacman1.png")
        
        self.x = 50
        self.y = 50
        
        
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
    
    
    def move_pacman(self):            
        if self.ylos:
            if self.y >0:
                self.y -= 1
    
        if self.alas:
            if self.y < 1000-self.pacman.get_height():
                self.y += 1
        
        if self.oikealle:
            if self.x <1000-self.pacman.get_width():
                self.x += 1
        if self.vasemmalle:
            if self.x >0:
                self.x -= 1
                
        
    
    
    
#kutsutaan ohjelmaa

#peli = Pacman()
#while True:
    #peli.handle_events()
    #peli.move_pacman()
    #peli.nayton_luominen()
    
            

        
        
        
        
                
    
    
        
        