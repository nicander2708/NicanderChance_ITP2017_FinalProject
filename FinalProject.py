import pygame
from pygame import*
from pygame.mixer import*
import random
import menu
def fproject():
#create the class for the enemy flakes
    class Enemy(sprite.Sprite):
        def __init__(self):
            sprite.Sprite.__init__(self)
            self.image = Surface( (11,11) )
            self.rect = self.image.get_rect()
            draw.line(self.image,Color("red"),(5,0),(5,10))
            draw.line(self.image,Color("red"),(0,2),(10,8))
            draw.line(self.image,Color("red"),(0,8),(10,2))
            draw.line(self.image,Color("red"),(10,5),(0,5))
            self.vy = 1
            enemies.add(self)
        def update(self):
            self.rect.y += self.vy
            self.rect.x = (self.rect.x+ self.vy)%width
            if self.rect.y > height-50:
                enemies.remove(self)
            if snow.lives>0 and self.rect.colliderect(snow.rect):
                snow.lives -= 1
                music.load('crash.wav')
                music.play(loops= 1)
                startlevel()

    #create the class for our main character
    class Snow(sprite.Sprite):
        def __init__(self):
            sprite.Sprite.__init__(self)
            self.image = Surface( (11,17) )
            self.rect = self.image.get_rect()
            poly = ((0,1),(2,4),(8,4),(10,1),(10,8),(7,10),(10,16),(0,16),(3,10),(0,8))
            draw.line(self.image,Color("blue"),(5,0),(5,10))#draw.line is used to draw a line
            draw.line(self.image,Color("blue"),(0,2),(10,8))
            draw.line(self.image,Color("blue"),(0,8),(10,2))#3 of these lines form a 6 pointed star that looks like a flake
            self.lives = 12
        def update(self):
            tasten = key.get_pressed()#this will trigger an action when a key gets pressed
            if tasten[K_UP]:
                self.rect.y -=  3
            if tasten[K_DOWN] and self.rect.bottom<height:
                self.rect.y += 3
            if tasten[K_LEFT] and self.rect.x>0:
                self.rect.x -= 3
            if tasten[K_RIGHT] and self.rect.right<width:
                self.rect.x += 3
            if (tasten[K_l]and self.rect.bottom<height) or self.rect.top<25:
                startlevel(min(level+1,len(vxranges)))

    enemies = sprite.RenderPlain()
    pygame.init()
    mixer.init()
    width = 800
    height = 600
    screen = display.set_mode((width,height))
    pygame.display.set_caption('Escape the snowflake army')
    clock = time.Clock()#this variable sets the app to run on a clock's time system
    snow = Snow()

    class Background():
        def __init__(self, imagefile):
            self.display = pygame.display.set_mode((800,600))
            self.image = image.load(imagefile)
            self.display.blit((self.image,(0,0)))


    #setting positions at which enemy flakes will spawn
    vxranges = ((0,0),(0,0),(-1,1),(1,2),(0,0),(1,1),(1,1),(2,2),(-2,2),(-2,2),(-2,2),(-3,3),(0,0))
    vyranges = ((1,1),(1,2),(1,2),(1,1),(1,3),(1,3),(1,3),(1,2),(1,3),(1,2),(1,2),(1,3),(0,0),(1,3))
    freqs = (0.1,0.1,0.1,0.1,0.2,0.2,0.25,0.25,0.3,0.3,0.4,0.4,0)
    #create a function that will constantly update the enemy movement and direction randomly
    def updateFlakes():
        if random.random()<freqs[level-1]:
            f = Enemy()
            f.rect.x = random.randint(0,3*width)
            f.rect.bottom = 0
            f.vx = random.randint(*vxranges[level-1])
            f.vy = random.randint(*vyranges[level-1])# by importing random library, randint will randomize the spawning
                                                        #of the enemy flakes
        enemies.update()
    #define a function for the level system
    def startlevel(lvl= 0):
        global level#global variable is used so that it can be used outside or inside the loop
        snow.rect.x = width/2
        snow.rect.bottom = height
        if lvl:
            level = lvl
            for x in range(800):
                updateFlakes()#this calls the function to randomize the speed and movement of the enemy flakes each level
    startlevel(1)
    while True:
        for x in event.get():
            if x.type == QUIT:
                pygame.quit()
                break
        bg = image.load('plains.jpeg')
        screen.blit(bg,(0,0))
        myfont = pygame.font.SysFont("Comic Sans Ms", 25)
        textsurface = myfont.render('Lives: %d'%snow.lives, True, (255, 255, 255))
        screen.blit(textsurface,(width-120,20))
        if level<len(vxranges):
            myfont = pygame.font.SysFont("Comic Sans Ms", 25)
            textsurface = myfont.render('Level:%d/%d'%(level,len(vxranges)-1), True, (255, 255, 255))
            screen.blit(textsurface,(width-120,50))
            updateFlakes()
            enemies.draw(screen)
            if level >= 5:
                bg1 = image.load('sky.jpeg')
                screen.blit(bg1,(0,0))
                myfont = pygame.font.SysFont("Comic Sans Ms", 25)
                textsurface = myfont.render('Level:%d/%d'%(level,len(vxranges)-1), True, (255, 255, 255))
                screen.blit(textsurface,(width-120,50))
                myfont = pygame.font.SysFont("Comic Sans Ms", 25)
                textsurface = myfont.render('Lives: %d'%snow.lives, True, (255, 255, 255))
                screen.blit(textsurface,(width-120,20))
                updateFlakes()
                enemies.draw(screen)
        else:
            myfont = pygame.font.SysFont("Comic Sans Ms", 25)
            textsurface = myfont.render('Congratulations, you won!m',False, (255, 255, 255))
            screen.blit(textsurface,(100,100))
            myfont = pygame.font.SysFont("Comic Sans Ms", 25)
            textsurface = myfont.render('play again by pressing \'n\'',False, (255, 255, 255))
            screen.blit(textsurface,(100,300))
            myfont = pygame.font.SysFont("Comic Sans Ms", 25)
            textsurface = myfont.render('or press m to go back to main menu',False, (255, 255, 255))
            screen.blit(textsurface,(100,450))

        if snow.lives>0:
            snow.update()
            screen.blit(snow.image,snow.rect.topleft)
        else:
            myfont = pygame.font.SysFont("Comic Sans Ms", 20)
            textsurface = myfont.render('Game over',False, (255, 255, 255))
            screen.blit(textsurface,(1,height/2))
            myfont = pygame.font.SysFont("Comic Sans Ms", 20)
            textsurface = myfont.render('Start new game by pressing \'n\'  ',False, (255, 255, 255))
            screen.blit(textsurface,(1,height/2+20))
            myfont = pygame.font.SysFont("Comic Sans Ms", 20)
            textsurface = myfont.render('Return to main menu by pressing \'m\'  ',False, (255, 255, 255))
            screen.blit(textsurface,(1,height/2+40))
        if key.get_pressed()[K_n]:#this will command will trigger an action which is starting a new game by pressing key 'n'
            snow.lives = 12
            startlevel(1)
        if key.get_pressed()[K_m]:
            menu.main()
        if level==1 and snow.lives==12 and snow.rect.bottom==height:
            myfont = pygame.font.SysFont("Comic Sans Ms", 20)
            textsurface = myfont.render('You are the sole survivor of the Blue Flakes.You must escape before the white flakes surround and capture you', False, (255, 255, 255))
            screen.blit(textsurface,(1,300))
            myfont = pygame.font.SysFont("Comic Sans Ms", 20)
            textsurface = myfont.render('You must escape before the army of black flakes surround and capture you', False, (255, 255, 255))
            screen.blit(textsurface,(1,500))
        display.update()
        clock.tick(60)#60 here refers to how fast the program will run in terms of speed.
fproject()

