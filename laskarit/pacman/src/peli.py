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
                
#https://www.google.com/search?q=pacman+png&client=ubuntu&channel=fs&tbm=isch&source=iu&ictx=1&vet=1&fir=93Fx76witA-fsM%252CJhLsJm4wb-nK7M%252C_%253BO3-lXMo2s7jmrM%252CN2v0RNaiyVTd2M%252C_%253BHAZYL6xT8RsYYM%252CE1OxMFWO2VwvsM%252C_%253ByBq6tYBoK4vYTM%252CHZbO3rl-BiNtFM%252C_%253B2uArZ3tjyjxB2M%252COujEZRiWP9HYyM%252C_%253B3MRa_wTfSdjKPM%252CD9r-JFlfiDshmM%252C_%253BWuABiZMtoWVoIM%252CFZDfareVgP_8kM%252C_%253BNF_mZTaiHmf7_M%252CZGTpx05sQgqAxM%252C_%253B0r5CEpIJIO4jSM%252CdnXPedgMXq4-rM%252C_%253BPiPQU1ldH8ap6M%252CfA9ZiSxZiniCpM%252C_%253BF7OVdVXdvpBoiM%252CE3rF3QMHofR1VM%252C_%253B9ygBToAaNVZCKM%252CzgA3t9u_NrQVvM%252C_%253B61E0weVfWSpi5M%252CZDxRk-2c8vsryM%252C_%253BN2NynA_7t7H8tM%252CdAyWY0dKhkgibM%252C_%253BZDIlLzgKjoH2lM%252CJhLsJm4wb-nK7M%252C_&usg=AI4_-kSoo2uyDO9Kwgd-ber3959pHwfWVg&sa=X&ved=2ahUKEwiwyKSp6P32AhWKr4sKHewgDd0Q9QF6BAgfEAE#imgrc=yBq6tYBoK4vYTM
#kuva 
                
        
    
    
    
#kutsutaan ohjelmaa

#peli = Pacman()
#while True:
#    peli.handle_events()
#    peli.move_pacman()
#    peli.nayton_luominen()
    
            

        
        
        
        
                
    
    
        
        