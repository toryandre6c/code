# Import the pygame library and initialise the game engine
import pygame
#Let's import the piece Class
from piece import Piece
#Let's import the player Class
from player import Player
from board import Board
pygame.init()
player1 = 1
player2 = 2
active_player = player1
# Open a new window
size = (700, 486)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

# background image
background = pygame.image.load("brierre_path.jpg")

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
player1_group = pygame.sprite.Group()
player2_group = pygame.sprite.Group()
board_group = pygame.sprite.Group()


player1_p1 = Piece(1,40,100)
player1_p2 = Piece(2,40,250)
player1_p3 = Piece(3,40,400)
# Add the Piece to the list of objects
all_sprites_list.add(player1_p1)
all_sprites_list.add(player1_p2)
all_sprites_list.add(player1_p3)

player1_group.add(player1_p1)
player1_group.add(player1_p2)
player1_group.add(player1_p3)

# player 2 cordinate
player2_p10 = Piece(8,600,100)
player2_p11 = Piece(9,600,250)
player2_p12 = Piece(10,600,400)
# Add the Piece to the list of objects
all_sprites_list.add(player2_p10)
all_sprites_list.add(player2_p11)
all_sprites_list.add(player2_p12)

player2_group.add(player2_p10)
player2_group.add(player2_p11)
player2_group.add(player2_p12)

player1 = Player("Tory", 1, player1_p1)
player2 = Player("Andre", 2, player1_p1)

board = Board(1,115,0)
all_sprites_list.add(board)
board_group.add(board)
board = Board(2,315,0)
all_sprites_list.add(board)
board_group.add(board)
board = Board(3,515,0)
all_sprites_list.add(board)
board_group.add(board)
board = Board(4,115,203)
all_sprites_list.add(board)
board_group.add(board)
board = Board(5,315,203)
all_sprites_list.add(board)
board_group.add(board)
board = Board(6,515,203)
all_sprites_list.add(board)
board_group.add(board)
board = Board(7,115,406)
all_sprites_list.add(board)
board_group.add(board)
board = Board(8,315,406)
all_sprites_list.add(board)
board_group.add(board)
board = Board(9,515,406)
all_sprites_list.add(board)
board_group.add(board)



# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
prev_pressed = 0
curr_piece = None
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False # Flag that we are done so we exit this loop
    
    mouse_pressed = pygame.mouse.get_pressed()[0]
    mousex,mousey = pygame.mouse.get_pos()
    
    if prev_pressed == 0 and mouse_pressed == 1:
        for piece in player1_group: 
            if piece.rect.collidepoint(mousex,mousey):
                curr_piece = piece
                
        for piece in player2_group: 
            if piece.rect.collidepoint(mousex,mousey):  
                curr_piece = piece
    
    if mouse_pressed == 1:
        curr_piece.rect.x=mousex-curr_piece.rect.width/2
        curr_piece.rect.y=mousey-curr_piece.rect.height/2    
        
    
    # --- Game logic should go here
    screen.blit(background, (0, 0))    
        
    #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
    board_group.draw(screen)
    player1_group.draw(screen)
    player2_group.draw(screen)
    
    
    player1.showName(screen)
    player2.showName(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
    prev_pressed = mouse_pressed

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
        