# Snake Game - Based on Udemy Course
# https://www.udemy.com/python-game-development-creating-a-snake-game-from-scratch/learn/v4/overview

# Imported libraries
import pygame
import sys
import random
import time

check_errors = pygame.init()  # should be (6, 0), 6 is processes initialized, 0 is errors
if check_errors[1] > 0 : 
    print("Error!: Had {0} initializing errors, quitting ...".format(check_errors[1]))
    print("Errors: " + str(check_errors))
else :
    print("(+) Pygame successfully intialized!")

# Play Surface
playSurface = pygame.display.set_mode((720,460))
pygame.display.set_caption('Snake Game')
time.sleep(5)

# Colors
red = pygame.Color(255,0,0)         # Game over
green = pygame.Color(0,255,0)       # Snake
black = pygame.Color(0,0,0)         # Score
white = pygame.Color(255,255,255)   # Background
brown = pygame.Color(165,42,42)     # Food

# FPS (Frames Per Second) Controller
fpsController = pygame.time.Clock()

# Important Variables
snakePos = [100,50]         # x,y of head
snakeBody = [[100,50],[90,50],[80,50]]  # Initially the snake has 3 blocks

# Food Position: x,y values are random and multiples of 10
foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10 ]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

score = 0
speed = 10
# Game Over Function
def gameOver() :
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game Over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOsurf, GOrect)
    showScore(2)
    pygame.display.flip()
    time.sleep(5)   # display for 5 seconds
    pygame.quit()   # pygame exit
    sys.exit()      # console exit

def showScore(choice=1) :
    sFont = pygame.font.SysFont('monaco', 24)
    Ssurf = sFont.render("Score: {0}".format(score), True, black)
    Srect = Ssurf.get_rect()
    if choice == 1 :
        Srect.midtop = (80, 10)     # Upper left corner
    else :
        Srect.midtop = (360, 120)   # Below game over message
    playSurface.blit(Ssurf, Srect)

# Main logic of the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()

        # Add code 1: Check for KEYDOWN
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE :
                pygame.event.post(pygame.event.Event(pygame.QUIT))


    
    # Add code 2: Validation of direction
    if changeto == 'RIGHT' and not direction == 'LEFT' :
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT' :
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN' :
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP' :
        direction = 'DOWN'



    if direction == "RIGHT":
        snakePos[0] += 10
    elif direction == "LEFT":
        snakePos[0] -= 10
    elif direction == "UP":
        snakePos[1] -= 10
    elif direction == "DOWN":
        snakePos[1] += 10



    # Add Code 4: Snake body mechanism, the snake moves to the new snakePos, check for food
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1] :
        foodSpawn = False   # The snake ate the food
        score += 1
        if score % 10 == 0:
            speed += 2        
    else :
        snakeBody.pop()

    

    # Add Code 5: Check if there is food
    if foodSpawn == False :
        foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10 ]
        foodSpawn = True

    
    
   # Add code 6: make the play surface background white
    playSurface.fill(white)

    

    # Add code 7: draw snake
    for pos in snakeBody :
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))   # Rect(x, y, size_x, size_y)

    

    # Add code 8: draw food
    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    

    # Add code 9: Check if the snake is out of bounds
    if snakePos[0] > 710:
        snakePos[0] = 0
    elif snakePos[0] < 0:
        snakePos[0] = 710 
    elif snakePos[1] > 450:
        snakePos[1] = 0 
    elif snakePos[1] < 0 :
        snakePos[1] = 450 

    

    # Add code 10: Check if snake runs into itself
    for block in snakeBody[1:] :    # snakeBody[0] is the head
        if snakePos[0] == block[0] and snakePos[1] == block[1] :
            hn0-gameOver()

    

    # Add code 11: update the display
    showScore()
    pygame.display.flip()
    fpsController.tick(speed)


