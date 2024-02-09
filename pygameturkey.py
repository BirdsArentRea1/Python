import pygame
pygame.init()
pygame.display.set_caption("Turkey")
screen = pygame.display.set_mode((1000, 1000))

RED = (250,0,0)
ORANGE = (200, 100, 0)
BROWN = (110, 70, 0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0, 0, 0)

while(1):
    screen.fill((0, 0, 0))

    #feathers left
    pygame.draw.circle(screen, (ORANGE), (250, 600), 80)
    pygame.draw.circle(screen, (RED), (300, 500), 80)
    pygame.draw.circle(screen, (ORANGE), (350, 400), 80)
    pygame.draw.circle(screen, (RED), (400, 350), 80)
    #feathers right
    pygame.draw.circle(screen, (RED), (680, 600), 80)
    pygame.draw.circle(screen, (ORANGE), (660, 500), 80)
    pygame.draw.circle(screen, (RED), (600, 400), 80)
    pygame.draw.circle(screen, (ORANGE), (500, 350), 80)
    #legs
    pygame.draw.rect(screen, (ORANGE), (400, 770, 20, 100)) 
    pygame.draw.rect(screen, (ORANGE), (520, 770, 20, 100))
    #body
    pygame.draw.circle(screen, (BROWN), (475, 600), 200)
    pygame.draw.ellipse(screen, (BROWN), (400, 300, 150, 300))
    #beak
    pygame.draw.polygon(screen, (YELLOW), ((450,350), (470,400), (500,350)))  
    #eyes
    pygame.draw.circle(screen, (WHITE), (450, 350), 20)
    pygame.draw.circle(screen, (BLACK), (450, 350), 10)
    pygame.draw.circle(screen, (WHITE), (500, 350), 20)
    pygame.draw.circle(screen, (BLACK), (500, 350), 7)
       
    
    
    pygame.display.flip()
