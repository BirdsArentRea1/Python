import pygame #bring in pygame library
pygame.init() #initialize pygame

screen = pygame.display.set_mode((800, 800)) #create game screen
pygame.display.set_caption("A lovely House!") #window title

pygame.draw.rect(screen, (0, 100, 200), (0, 0, 800, 800))#house
pygame.draw.rect(screen, (90, 90, 90), (200, 600, 500, 300))#house
pygame.draw.rect(screen, (100, 50,0), (425, 700, 50, 100))#door
pygame.draw.rect(screen, (0, 70,100), (300, 700, 70, 70))#window
pygame.draw.rect(screen, (0, 70,100), (550, 700, 70, 70))#window2
pygame.draw.circle(screen, (200, 200, 0), (100, 100), 50)#sun
pygame.draw.polygon(screen, (80, 50, 0), ((200, 600), (700, 600), (410, 280)))#roof
pygame.draw.rect(screen, (90, 40,0), (75, 600, 70, 300))#treetrunk
pygame.draw.circle(screen, (0, 100, 25), (100, 620), 50)#leaves
pygame.draw.circle(screen, (0, 100, 25), (100, 560), 50)#leaves
pygame.draw.circle(screen, (0, 100, 25), (100, 500), 50)#leaves
pygame.draw.circle(screen, (0, 100, 25), (50, 530), 50)#leaves
pygame.draw.circle(screen, (0, 100, 25), (150, 530), 50)#leaves
pygame.draw.circle(screen, (0, 100, 25), (150, 600), 50)#leaves
pygame.draw.circle(screen, (0, 100, 25), (50, 600), 50)#leaves


pygame.display.flip() #update graphics 
