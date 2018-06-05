import pygame
class Player():
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    name = " "
    player_No = 0
    def __init__(self, name, player_No,  player_pieces):
        # Call the parent class (Sprite) constructor
        #super().__init__()

        #Initialise attributes of the Piece.
        self.name = name
        self.player_No = player_No
        
    def showName(self, screen) :
        NFont = pygame.font.SysFont('monaco', 38)
        Nsurf = NFont.render(self.name, True, (0,0,0))
        Nrect = Nsurf.get_rect()
        if self.player_No == 1 :
            Nrect.x = 40 
            Nrect.y = 10
        else :
            Nrect.x = 600 
            Nrect.y = 10
        screen.blit(Nsurf, Nrect)        
'''        

Player1 = player(x)
Player2 = player(y)
print(Player1.name)        
print(Player2.name)

# Fetch the rectangle object that has the dimensions of the image.
self.rect = self.image.get_rect()
self.rect.x = x
self.rect.y = y
'''