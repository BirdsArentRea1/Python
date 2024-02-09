import pygame
import math #needed for square root function

isBig = False

pygame.init()#initializes Pygame
print(pygame.font.get_fonts())
pygame.display.set_caption("Cookie Clicker")#sets the window title
screen = pygame.display.set_mode((400,400))#creates game screen

CookiePic = pygame.image.load("cookie.jpg")
CookieRect = CookiePic.get_rect(topleft=(60,60))

click = pygame.mixer.Sound('birb.wav')

print(pygame.font.get_fonts())
#player variables
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
numClicks = 0

#circle variables: circX and circY are the coordinates of the center (where it's drawn), and the radius is how big it is
circX = 200
circY = 200
radius = 100

font = pygame.font.Font('freesansbold.ttf', 32)
text1 = font.render('score:',False, (0,200,200))
text2 = font.render(str(int(numClicks)), 1, (0,200,200))

CookiePic = pygame.image.load("cookie.jpg")
CookieRect = CookiePic.get_rect(topleft=(75,75))

CookiePic2 = pygame.image.load("cookie2.jpg")
CookieRect2 = CookiePic2.get_rect(topleft=(50 ,50))

#gameloop###################################################
while True:
#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()
    
    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN: #check if clicked
        mousePos = event.pos
        print("mouse position: (",mousePos[0]," , ",mousePos[1], ")")
        if math.sqrt((circX - mousePos[0])**2 + (circY - mousePos[1])**2) <radius:
            numClicks+=1
            print("CLICK")
            isBig = True
    else:
        isBig = False
        
    if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.mixer.Sound.play(click)
 
#render section---------------------------------------------
    screen.fill((255, 255, 255)) #wipe screen (without this, things smear)
    
    pygame.draw.circle(screen, (200, 0, 200), (circX,circY), radius)
    #print("clicks:", numClicks) #uncomment this once collision is set up
    
    text2 = font.render(str(int(numClicks)), 1, (0, 200, 200))
    screen.blit(text1, (10, 10))
    screen.blit(text2, (110, 10))

    #screen.blit(CookiePic, CookieRect)
    if isBig == True:
        screen.blit(CookiePic, CookieRect)
    else:
        screen.blit(CookiePic2, CookieRect)
        
    pygame.display.flip()
    

#end game loop##############################################

pygame.quit()
