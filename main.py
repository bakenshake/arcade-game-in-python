"""
Arcade Game in Python
Created by: Kati Baker for Code Camp 2023
Date: 12/29/22
"""
import pygame #tells our compiler (Visual Studio Code) to pull the pygame library into our Python file
import random
import math

#Initializes pygame library
pygame.init()

#Set the height and width of our game screen (width, height)
#(0,0) starts in our top left corner
screen = pygame.display.set_mode((800, 600))

#Set the title of our game screen
pygame.display.set_caption("Arcade Game at Code Camp 2023")

#Set the icon of our game screen
game_icon = pygame.image.load("assets/player/playerShip1_orange.png") #what's inside quotations has to match the path of where the image is
pygame.display.set_icon(game_icon)

#Score keeping!
score = 0

##########
# Player #
##########

#Setting the image for the player
player_image = game_icon

#Player starting position
player_x = 370
player_y = 480

#Tracking Player coordinate changes
playerX_change = 0

#########
# Enemy #
#########
#Enemy image
enemy_image = pygame.image.load("assets/enemies/ship_E.png")
#enemy_image = pygame.transform.flip(enemy_image, False, True)

#Enemy army 
enemy_image = []
enemy_x = []
enemy_y = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(0,num_of_enemies):
    #we need this line to make the ships face the correct direction aka down towards the player
    enemy_image.append(pygame.image.load("assets/enemies/ship_E.png"))

    #Coordinates for the enemy
    enemy_x.append(random.randint(0,800))
    enemy_y.append(random.randint(50,150))
    enemyX_change.append(0.3)
    enemyY_change.append(5)

##########
# Bullet #
##########

#Ready - You can't see the bullet on the screen
#Fire - The bullet is currently moving
bullet_image = pygame.image.load("assets/player/star_tiny.png")
bullet_x = 0
bullet_y = 480
bulletX_change = 0
bulletY_change = 2
bullet_state = "ready"

#We use a different x and y so we can pass in different variables to this function
def player(x,y):
    screen.blit(player_image, (x, y))

def enemy(x,y,i):
    screen.blit(enemy_image[i], (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x+16,y+10)) #need the 16 and 10 to show the bullet at the nose

def check_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x-bullet_x,2)) + (math.pow(enemy_y-bullet_y,2)))
    if distance < 20:
        return True
    else:
        return False
"""
Game Logic
Summary: Logic to keep the game screen running until the player hits the close window button
"""
game_running = True
while game_running:
    #Changes background color of the game screen using RGB (red, green, blue)
    screen.fill((0,0,0))
    
    #Game Logic to exit our game and move our player - all our input
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #this pygame.QUIT is referencing the pygame library
            game_running = False

        #Tracking Keyboard Input so our player can move
        #Keyboard keys are called events in pygame (see above for quitting the game)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #to quit via escape
                game_running = False
            if event.key == pygame.K_LEFT: #for moving to the left
                print("Left key pressed")
                playerX_change = -1.5
            if event.key == pygame.K_RIGHT:
                print("Right key presed")
                playerX_change = 1.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
                
        if event.type == pygame.KEYUP: #when we release the arrow keys
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Key released")
                playerX_change = 0

    player_x += playerX_change

    #Keeps our player in bounds
    #Note: The exact number will vary depending on the size of the player sprite you chose to use!
    if player_x <= 0:
        player_x = 0
    elif player_x >= 701:
        player_x = 701

    player(player_x,player_y)

    #Enemy Movement
    for i in range(0,num_of_enemies):

        if enemy_y[i] > 200:
            for j in range(0,num_of_enemies):
                enemy_y[j] = 2000
            print("GAME OVER")
            break
        enemy_x[i] += enemyX_change[i]
        if enemy_x[i] <= 0:
            enemyX_change[i] = 0.3
            enemy_y[i] += enemyY_change[i]
        elif enemy_x[i] >= 736:
            enemyX_change[i] = -0.3
            enemy_y[i] += enemyY_change[i]

        #Collision Checking
        collision = check_collision(enemy_x[i],enemy_y[i],bullet_x,bullet_y)
        if collision:
            #reset the bullet
            bullet_y = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemy_x[i] = random.randint(0,800)
            enemy_y[i] = random.randint(50,150)

        enemy(enemy_x[i],enemy_y[i], i)

    #Bullet Movement
    if bullet_y <=0:
        bullet_y = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bulletY_change

    #We have to tell pygame to update the game screen with the changes that we've made
    pygame.display.update()