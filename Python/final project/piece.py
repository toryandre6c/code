import pygame

class Piece(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, x,  y):
        # Call the parent class (Sprite) constructor
        super().__init__()

        #Initialise attributes of the Piece.
        self.color = color

        # Instead we could load a proper picture of a Piece...
        if  self.color == 1:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_001.png").convert_alpha()
        elif self.color == 2:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_002.png").convert_alpha()
        elif self.color == 3:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_003.png").convert_alpha()
        elif self.color == 4:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_004.png").convert_alpha()
        elif self.color == 5:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_005.png").convert_alpha()
        elif self.color == 6:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_006.png").convert_alpha()
        elif self.color == 7:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_007.png").convert_alpha()
        elif self.color == 8:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_008.png").convert_alpha()
        elif self.color == 9:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_009.png").convert_alpha()
        elif self.color == 10:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_010.png").convert_alpha()
        elif self.color == 11:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_011.png").convert_alpha()
        elif self.color == 12:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_012.png").convert_alpha()
        elif self.color == 13:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_013.png").convert_alpha()
        elif self.color == 14:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_014.png").convert_alpha()
        elif self.color == 15:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_015.png").convert_alpha()
        elif self.color == 16:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_016.png").convert_alpha()
        elif self.color == 17:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_017.png").convert_alpha()
        elif self.color == 18:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_018.png").convert_alpha()
        elif self.color == 19:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_019.png").convert_alpha()
        elif self.color == 20:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_020.png").convert_alpha()
        elif self.color == 21:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_021.png").convert_alpha()
        elif self.color == 22:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_022.png").convert_alpha()
        elif self.color == 23:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_023.png").convert_alpha()
        elif self.color == 24:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_024.png").convert_alpha()
        elif self.color == 25:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_025.png").convert_alpha()
        elif self.color == 26:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_026.png").convert_alpha()
        elif self.color == 27:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_027.png").convert_alpha()            
        else:
            self.image = pygame.image.load("Gems_01/Gems_01_64x64_028.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        

  