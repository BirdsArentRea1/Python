import pygame
pygame.init()  
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

mariobackround = pygame.image.load('mariobackround.png')
Link = pygame.image.load('link.png') #load your spritesheet
Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3
#A=0
#D=1
#W = 2




#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform
health = 100

#player variables
#xpos2 = 500 #xpos of player
#ypos2 = 200 #ypos of player
#vx = 0 #x velocity of player
#vy2 = 0 #y velocity of player
#keys2 = [False, False, False, False] #this list holds whether each key has been pressed
#isOnGround2 = False #this variable stops gravity from pulling you down more when on a platform

#enemies are held as a LIST. Lists have square brackets []
#you already know variables are storage boxes. Lists are storage boxes with slots in them!
enemy1 = [200, 630, 0] # each monster has a xpos, ypos, and ticker
enemy2 = [400, 780, 45]
enemy3 = [250, 630, 45]

def enemyMove(enemyInfo):
    #print(enemyInfo)
    enemyInfo[2]+=1
    if enemyInfo[2] <= 40:
        enemyInfo[0] += 1
    elif enemyInfo[2] <= 80:
        enemyInfo[0] -=1
    else:
        enemyInfo[2] = 0 #reset timer
        
def enemyMove2(enemyInfo):
    #print(enemyInfo)
    enemyInfo[2]+=1
    if enemyInfo[2] <= 40:
        enemyInfo[1] += 1
    elif enemyInfo[2] <= 80:
        enemyInfo[1] -=1
    else:
        enemyInfo[2] = 0 #reset timer
        
def enemyCollide(enemyInfo, playerX, playerY):
    if playerX+20>enemyInfo[0]: #right side of player, left side of enemy
        if playerX < enemyInfo[0]+20: #left sdie of player, right side of enemy
            if playerY < enemyInfo[1]+20: #top of the player, bottom of the enemy
                if playerY+20 > enemyInfo[1]:
                    return True
    else:
        return False

frameWidth = 64
frameHeight = 96
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0


while not gameover and health > 0: #GAME LOOP############################################################
    clock.tick(60) #FPS
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
            
        
      
        if event.type == pygame.KEYDOWN: #looks for key presses
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            if event.key == pygame.K_a:
                   keys2[a]=True                
            if event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
            if event.key == pygame.K_d:
                keys2[d]=True
            if event.key == pygame.K_UP:
                keys[UP]=True
            if event.key == pygame.K_w:
                keys[w]=True
                

        elif event.type == pygame.KEYUP: #looks for key releases
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
            elif event.key == pygame.K_UP:
                keys[UP]=False
            elif event.key == pygame.K_w:
                keys2[w]=True
            elif event.key == pygame.K_a:
                keys2[a]=True
            elif event.key == pygame.K_d:
                keys2[d]=True

    #physics section--------------------------------------------------------------------
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        direction = LEFT
        
    elif keys[RIGHT]==True:
        vx =+3
    #turn off velocity
    else:
        vx = 0
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP
    #if keys2[a]==True:
        #vx=-3
        #direction = a
    #elif keys2[d]==True:
        #vx =+3
    #if keys2[w] == True and isOnGround == True: #only jump when on the ground
        #vy = -8
        #isOnGround = False
        #direction = w
    #function call for enemy movement
    enemyMove(enemy1)

        
    enemyMove(enemy2)


    enemyMove(enemy3)
    
    #check collision with enemies
    if enemyCollide(enemy1, xpos, ypos):
        print("hit")
        health  -=10
    if enemyCollide(enemy2, xpos, ypos):
        print("hit")
        health  -=10
    if enemyCollide(enemy3, xpos, ypos):
        print("hit")
        health  -=10
    
    #COLLISION
    if xpos>100 and xpos<200 and ypos+40 >750 and ypos+40 <770:
        ypos = 750-40
        isOnGround = True
        vy = 0
    elif xpos>200 and xpos<300 and ypos+40 >650 and ypos+40 <670:
        ypos = 650-40
        isOnGround = True
        vy = 0
    elif xpos>300 and xpos<400 and ypos+40 >550 and ypos+40 <570:
        ypos = 550-40
        isOnGround = True
        vy = 0
    elif xpos>400 and xpos<500 and ypos+40 >450 and ypos+40 <470:
        ypos = 450-40
        isOnGround = True
        vy = 0
    elif xpos>500 and xpos<600 and ypos+40 >350 and ypos+40 <370:
        ypos = 350-40
        isOnGround = True
        vy = 0
    elif xpos>600 and xpos<700 and ypos+40 >250 and ypos+40 <270:
        ypos = 250-40
        isOnGround = True
        vy = 0
    elif xpos>700 and xpos<800 and ypos+40 >150 and ypos+40 <170:
        ypos = 150-40
        isOnGround = True
        vy = 0
    else:
        isOnGround = False


    
    #stop falling if on bottom of game screen
    if ypos > 760:
        isOnGround = True
        vy = 0
        ypos = 760
        
    
    #if ypos2 > 760:
        #isOnGround2 = True
        #vy2 = 0
        #ypos2 = 760
    
    #gravity
    if isOnGround == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION
    #if isOnGround2 == False:
        #vy2+=.2

    #update player position
    xpos+=vx 
    ypos+=vy
    
    #xpos2+=vx 
    #ypos2+=vy
    
    #Animation----------------------------------------------------------------------------------------
    if vx < 0: #left animation
        # Ticker is a spedometer. We don't want Link animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
        RowNum = 0
        ticker+=1
        if ticker%10==0: #only change frames every 10 ticks
            frameNum+=1
           #If we are over the number of frames in our sprite, reset to 0.
           #In this particular case, there are 10 frames (0 through 9)
        if frameNum>7: 
            frameNum = 0
  
    if vx > 0: #left animation
        # Ticker is a spedometer. We don't want Link animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
        RowNum = 1
        ticker+=1
        if ticker%10==0: #only change frames every 10 ticks
            frameNum+=1
           #If we are over the number of frames in our sprite, reset to 0.
           #In this particular case, there are 10 frames (0 through 9)
        if frameNum>7: 
            frameNum = 0
           
    if vy < 0: #left animation
        # Ticker is a spedometer. We don't want Link animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
            RowNum = 2
            ticker+=1
            if ticker%10==0: #only change frames every 10 ticks
                frameNum+=1
           #If we are over the number of frames in our sprite, reset to 0.
           #In this particular case, there are 10 frames (0 through 9)
            if frameNum>7: 
                frameNum = 0
           
             
    if vy > 0: #left animation
        # Ticker is a spedometer. We don't want Link animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
        RowNum = 3
        ticker+=1
        if ticker%10==0: #only change frames every 10 ticks
            frameNum+=1
           #If we are over the number of frames in our sprite, reset to 0.
           #In this particular case, there are 10 frames (0 through 9)
        if frameNum>7: 
            frameNum = 0
    
  
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    screen.blit(mariobackround, (300, 400))
    screen.blit(Link, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))

    
    pygame.draw.rect(screen, (255,255,255), (enemy1[0], enemy1[1], 20, 20)) #access first and second slot of LIST
    pygame.draw.rect(screen, (255,255,255), (enemy2[0], enemy2[1], 20, 20))
    pygame.draw.rect(screen, (255,255,255), (enemy3[0], enemy3[1], 20, 20))
    
    #platforms
    pygame.draw.rect(screen, (200, 0, 10), (100, 750, 100, 20))
    pygame.draw.rect(screen, (200, 0, 20), (200, 650, 100, 20))
    pygame.draw.rect(screen, (200, 0, 30), (300, 550, 100, 20))
    pygame.draw.rect(screen, (200, 0, 40), (400, 450, 100, 20))
    pygame.draw.rect(screen, (200, 0, 50), (500, 350, 100, 20))
    pygame.draw.rect(screen, (200, 0, 60), (600, 250, 100, 20))
    pygame.draw.rect(screen, (200, 0, 70), (700, 150, 100, 20))
    
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
if health <=0:
    print("game over, you died")
pygame.quit()
