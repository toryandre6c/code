import pygame
board_piece_width = 70
board_piece_width_hight = 80
class Board(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, pos, x,  y):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Instead we could load a proper picture of a Piece.
        self.pos = pos 
        
        if  self.pos == 1:
            self.image = pygame.image.load("baron-samedi.jpg").convert_alpha()
            self.image = pygame.transform.scale(self.image, (board_piece_width, board_piece_width_hight))
        elif  self.pos == 2:
            self.image = pygame.image.load("occult.jpg").convert_alpha()
            self.image = pygame.transform.scale(self.image, (board_piece_width, board_piece_width_hight)) 
        elif  self.pos == 3:
            self.image = pygame.image.load("les-lois-palo-mayombe.jpg").convert_alpha()
            self.image = pygame.transform.scale(self.image, (board_piece_width, board_piece_width_hight))
        elif  self.pos == 4:
            self.image = pygame.image.load("spells.jpg").convert_alpha()
            self.image = pygame.transform.scale(self.image, (board_piece_width, board_piece_width_hight))
        elif  self.pos == 5:
            self.image = pygame.image.load("dantorezulie.jpg").convert_alpha()
            self.image = pygame.transform.scale(self.image, (board_piece_width, board_piece_width_hight))
        elif  self.pos == 6:
            self.image = pygame.image.load("veve.jpg").convert_alpha()
            self.image = pygame.transform.scale(self.image, (board_piece_width, board_piece_width_hight))
        elif  self.pos == 7:
            self.image = pygame.image.load("damballah.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (board_piece_width, board_piece_width_hight))
        elif  self.pos == 8:
            self.image = pygame.image.load("simbi.jpg").convert_alpha()
            self.image = pygame.transform.scale(self.image, (board_piece_width, board_piece_width_hight))        
        else:
            self.image = pygame.image.load("Ogoun-Veve.jpg").convert_alpha()
            self.image = pygame.transform.scale(self.image, (board_piece_width, board_piece_width_hight))

        
        
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        