import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("I hate sand")
clock = pygame.time.Clock()
mouseDown = False
mousePos = (0,0)
color = (200,0,0)

grid = [[0 for i in range(100)] for j in range(100)]

for i in range(100):
    for j in range(100):
        grid[i][j] = 0

grid[20][20]=1 #test block

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True

        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False

        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos

    #print(mouseDown)
    if mouseDown == True:

        grid[int(mousePos[0]/10)][int(mousePos[1]/10)]=1

    for k in range(99):
        for i in range(99):
            if grid[i][98-k]==1 and grid[i][99-k]==0:
               grid[i][98-k] = 0
               grid[i][99-k] = 1 

    screen.fill((100,100,100))

    for i in range(100):
        for j in range(100):

            if grid[i][j]==1:
                pygame.draw.rect(screen, (color), (i*10, j*10, 10, 10))
            else:
                pygame.draw.rect(screen,(255,255,255), (i*10, j*10, 10, 10))

    pygame.display.flip()

pygame.quit()
    
