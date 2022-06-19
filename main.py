import pygame
import random
import math

# initialize the pygame

pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("galaxy.jpg")

# title and icon
icon = pygame.image.load("ufo.png")
pygame.display.set_icon((icon))
pygame.display.set_caption("Space Invaders")

# player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# enemy

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):



    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(25, 710))
    enemyY.append(60)
    enemyX_change.append(0.3)
    enemyY_change.append(0.3)


# bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = playerX
bulletY = 480
bulletY_change = 0.7
bullet_state = "Ready"

# score
score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)

textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score :" + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))


def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def bullet(x,y):
    global bullet_state
    bullet_state="Fire"
    screen.blit(bulletImg,(x,y))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY-bulletY , 2)))
    if distance < 28:
        return True
    else:
        return False
    print(distance)


def gameOver(enemyX,enemyY,playerX,playerY):
    distance = math.sqrt((math.pow(enemyX - playerX,2)) + (math.pow(enemyY-playerY , 2)))
    if distance < 28:
        gameovertext = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(gameovertext, (200, 200))
        return True
    else:
        return False
    print(distance)



# game loop
running = True
while running:
    # set rgb fill
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0) )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # check keystroke
    if event.type == pygame.KEYDOWN:


        if event.key == pygame.K_LEFT:
            print("Left is pressed")
            playerX_change = -0.3
        if event.key == pygame.K_RIGHT:
            print("Right is pressed")
            playerX_change = 0.3


        if event.key == pygame.K_UP:
            print("Up is pressed")
            playerY_change = -0.3
        if event.key == pygame.K_DOWN:
            print("Right is pressed")
            playerY_change = 0.3

        if event.key == pygame.K_UP:
            if bullet_state is "Ready":
                bulletX = playerX
                bulletY = playerY
                bullet(bulletX,bulletY)
                print("fire!")


    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            print("Key is released")
            playerX_change = 0

        if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
            playerY_change = 0



    playerX += playerX_change
    playerY += playerY_change



    if playerX <= 0:
        playerX = 0
    elif playerX >736:
        playerX = 736

    for i in range(num_of_enemies):
        isover = gameOver(enemyX[i], enemyY[i], playerX, playerY)

        if enemyY[i] > 300 or isover == True:
            for j in range(num_of_enemies):
                enemyY[j]=2000
            gameOver(enemyX[i],enemyY[i],playerX,playerY)
            gameovertext = font.render("GAME OVER", True, (255, 255, 255))
            screen.blit(gameovertext, (300, 200))
            playerX = 2370
            playerY = 2480
            break


        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.1
            enemyY[i] += 50
        elif enemyX[i] > 736:
            enemyX_change[i] = -0.1
            enemyY[i] += 50

        enemy(enemyX[i],enemyY[i],i)

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = playerY
            bullet_state = "Ready"
            score_value += 1
            enemyX[i] = random.randint(25, 720)
            enemyY[i] = 60


    # bullet movement

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "Ready"
        print(bullet_state)

    if bullet_state == "Fire":
        bullet(bulletX,bulletY)
        bulletY -= bulletY_change


    print(score_value)

    player(playerX,playerY)

    show_score(370,40)

    pygame.display.update()



