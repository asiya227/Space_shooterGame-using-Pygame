import sys

import pygame
import random
import math
import button
import op
import asyncio
from pygame import mixer, K_w

mixer.init()
pygame.init()


mixer.music.load('Powerful-Trap-.mp3')
mixer.music.play(-1)

screen=pygame.display.set_mode((900,650))
pygame.display.set_caption('Space Shooter')
icon=pygame.image.load('space.png')
pygame.display.set_icon(icon)

background=pygame.image.load('img.png')
background=pygame.transform.scale(background, (900, 650))

spaceshipimg=pygame.image.load('spaceship.png')

alienimg=[]
alienX=[]
alienY=[]
alienspeedX=[]
alienspeedY=[]

no_of_aliens=6

for i in range(no_of_aliens):
    alienimg.append(pygame.image.load('alien.png'))
    alienX.append(random.randint(0,736))
    alienY.append(random.randint(25,100))
    alienspeedX.append(-1)
    alienspeedY.append(27)

score=0

bulletimg=pygame.image.load('bullet.png')
check=False
bulletX=406
bulletY=470

spaceshipX=390
spaceshipY=500
changeX=0

running=True

font=pygame.font.SysFont('Comic Sans MS',32,'bold')

def score_txt():                            #score increasing txt!!
    img=font.render(f'Score  : {score}',True,'white')
    screen.blit(img,(10,10))

font_gameover=pygame.font.SysFont('Chiller',72,'bold')

def gameover():
    img_gameover = font_gameover.render('G A M E  O V E R', True, 'white')
    screen.blit(img_gameover, (270, 270))


while running:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                changeX=-2
            if event.key==pygame.K_RIGHT:
                changeX=2
            if event.key == pygame.K_w:
                pygame.mixer.music.fadeout(1000)
            if event.key == pygame.K_e:
                pygame.mixer.music.play(-1)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()   #totally exit the screen (like window)
            if event.key == pygame.K_m:
                pygame.mixer.music.load("Clown.mp3")
                pygame.mixer.music.play(-1)
            if event.key == pygame.K_a:
                pygame.mixer.music.load("Powerful-Trap-.mp3")
                pygame.mixer.music.play(-1)
            if event.key==pygame.K_SPACE:               #bullet is fired here
                if check is False:
                    bulletSound=mixer.Sound('shot.wav')
                    bulletSound.play()
                    check=True
                    bulletX=spaceshipX+16

        if event.type==pygame.KEYUP:
            changeX=0
    spaceshipX+=changeX    #spaceshipX=spaceshipX-changeX
    if spaceshipX<=0:
        spaceshipX=0
    elif spaceshipX>=850:
        spaceshipX=850

    for i in range(no_of_aliens):
        if alienY[i] > 450:                             # to disappear the alien
            for j in range(no_of_aliens):
                alienY[j] = 2000
            gameover()
            break
        alienX[i]+=alienspeedX[i]
        if alienX[i]<=0:
            alienspeedX[i]=1
            alienY[i]+=alienspeedY[i]
        if alienX[i]>=850:
            alienspeedX[i]=-1
            alienY[i]+=alienspeedY[i]

        distance = math.sqrt(math.pow(bulletX - alienX[i], 2)) + math.sqrt(math.pow(bulletY - alienY[i], 2))
        if distance < 27:
            explosion = mixer.Sound('falling.wav')
            explosion.play()
            bulletY = 470
            check = False
            alienX[i] = random.randint(0, 736)  # moving back to original position
            alienY[i] = random.randint(25, 100)
            score += 1
        screen.blit(alienimg[i], (alienX[i], alienY[i]))

    if bulletY<=0:           #setting bullet position to up and again back to down(original position)
        bulletY=470
        check=False
    if check:                #setting ship posiyion
        screen.blit(bulletimg, (bulletX, bulletY))
        bulletY-=2

    screen.blit(spaceshipimg,(spaceshipX,spaceshipY))
    score_txt()

    pygame.display.update()

op.Option()
