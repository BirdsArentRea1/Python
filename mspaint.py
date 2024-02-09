import pygame
pygame.init()#initializes Pygame
pygame.display.set_caption("python paint program")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
draw = False
#color definitions (you have to add these to the game, and you can add more if you want)
BLUE = (0,0,200)
RED = (200, 0,0)
GREEN = (0,200, 0)
YELLOW = (200, 200, 0)
PURPLE = (200, 0, 200)
TEAL = (0,200,200)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
color = RED

BigSquare = 1
circle =2
SmallSquare = 3
shape = BigSquare
#gameloop###################################################
while True:
#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()
#update/timer section---------------------------------------    
    if mousePos[0] > 0 and mousePos[0] < 50 and mousePos[1] >750:
        color = RED
    if mousePos[0] > 50 and mousePos[0] < 100 and mousePos[1] >750:
        color = BLUE
    if mousePos[0] > 100 and mousePos[0] < 150 and mousePos[1] >750:
        color = GREEN
    if mousePos[0] > 150 and mousePos[0] < 200 and mousePos[1] >750:
         color = YELLOW
    if mousePos[0] > 200 and mousePos[0] < 250 and mousePos[1] >750:
         color = PURPLE
    if mousePos[0] > 250 and mousePos[0] < 300 and mousePos[1] >750:
         color = TEAL
    if mousePos[0] > 300 and mousePos[0] < 350 and mousePos[1] >750:
         color = WHITE
    if mousePos[0] > 350 and mousePos[0] < 400 and mousePos[1] >750:
         color = BLACK
    if mousePos[0] > 0 and mousePos[0] < 50 and mousePos[1] >650:
         shape =circle
    #add other colors here!
#input section----------------------------------------------
    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        draw = True

    if event.type == pygame.MOUSEBUTTONUP:
        draw = False

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
 
#render section---------------------------------------------
    if draw == True:
        if shape == circle:
            pygame.draw.circle(screen, color, (mousePos), 10) #player paintbrush
        elif shape == BigSquare:
          pygame.draw.rect(screen,color,(mousePos[0], mousePos[1], 50, 50))
    
    #color changing rectangles at bottom of screen 
    pygame.draw.rect(screen, RED, (0,750,50,50))
    pygame.draw.rect(screen, BLUE, (50, 750, 50, 50))
    pygame.draw.rect(screen, GREEN, (100, 750, 50, 50))
    pygame.draw.rect(screen, YELLOW, (150, 750, 50, 50))
    pygame.draw.rect(screen, PURPLE, (200, 750, 50, 50))
    pygame.draw.rect(screen, TEAL, (250, 750, 50, 50))
    pygame.draw.rect(screen, WHITE, (300, 750, 50, 50))
    pygame.draw.rect(screen, BLACK, (350, 750, 50, 50))
    
    #add shape options here (in white)
    pygame.draw.circle(screen, WHITE, (25, 700), 20)
    #more colors go here!
        
    pygame.display.flip()
    

#end game loop##############################################

pygame.quit()
