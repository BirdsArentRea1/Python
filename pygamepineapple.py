import pygame
pygame.init
 
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Pineapple")
mousePos = (400,400)

while True:
    event = pygame.event.wait()
    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
        print(mousePos)
        
        pygame.draw.ellipse(screen, (255, 210, 0), (250, 200, 310, 500))
        
        for i in range(-100,1000, 30):
            pygame.draw.line(screen, (0,0,0), (i,0), (i+800, 800), 4)
            
        for i in range(-100, 1000, 30):
            pygame.draw.line(screen, (0,0,0), (0, i+800), (800, i), 4)
            
        pygame.draw.polygon(screen, (0, 90, 70), ((290,278), (262, 130), (510, 270)))
        
        pygame.draw.polygon(screen, (0, 90, 70), ((290,278), (522, 130), (510, 270)))
        
        pygame.draw.polygon(screen, (0, 90, 70), ((300,270), (392, 103), (500, 265)))
        
        pygame.display.flip()
