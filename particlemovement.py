import pygame
import random
import math

pygame.init()

gamescreen = pygame.display.set_mode((900,900))
pygame.display.set_caption("Single Particle Movement")
clock = pygame.time.Clock()

xpos = []
ypos = []
xvel = []
yvel = []
#ticker = []

while True:
    clock.tick(60)
        
    for i in range(1):
        if len(xpos) < 100:

            velx = random.uniform(-1,1)
            vely = random.uniform(-1,1)

            magnitude = math.sqrt(velx**2 + vely**2)

            if magnitude != 0:
                normalizedvelx = 2 * velx / magnitude
                normalizedvely = 2 * vely / magnitude
            else:
                normalizedvelx = 0
                normalizedvely = 0
                    
            xpos.append(450)
            ypos.append(450)
            xvel.append(normalizedvelx)
            yvel.append(normalizedvely)
                  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        
    for i in range(len(xpos)):
        
        #acceleration = (ticker[i] / 100) ** 2
        #xvel[i] = normxvel[i] * acceleration * 8
        #yvel[i] = normyvel[i] * acceleration * 8
        #ticker[i] += 1
        
        xpos[i] += xvel[i]
        ypos[i] += yvel[i]
        
        if xpos[i] < 0 or xpos[i] > 900 or ypos[i] > 900:
                xpos[i] = 450
                ypos[i] = 450
            
                velx = random.uniform(-1,1)
                vely = random.uniform(-1,1)
        
                magnitude = math.sqrt(velx**2 + vely**2)
        
                if magnitude != 0:
                    normalizedvelx = 2 * velx / magnitude
                    normalizedvely = 2 * vely / magnitude
                else:
                    xvel[i] = 0
                    yvel[i] = 0
         
    gamescreen.fill((0,0,0))
    for i in range(len(xpos)):
        pygame.draw.circle(gamescreen, (255,255,255),(xpos[i], ypos[i]), 5)
    pygame.display.flip()
        
pygame.quit()
