"""
Arcade Game in Python
Created by: Kati Baker for Code Camp 2023
Date: 12/29/22
"""
import pygame #tells our compiler (Visual Studio Code) to pull the pygame library into our Python file

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

#Setting the player icon
player_image = game_icon

#Player starting position
player_x = 370
player_y = 480

#Tracking Player coordinate changes
playerX_change = 0

#We use a different x and y so we can pass in different variables to this function
def player(x,y):
    screen.blit(player_image, (x, y))

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
            if event.key == pygame.K_LEFT: #for moving to the left
                print("Left key pressed")
                playerX_change = -1.5
            if event.key == pygame.K_RIGHT:
                print("Right key presed")
                playerX_change = 1.5
            if event.key == pygame.K_UP:
                print("Up key pressed")
            if event.key == pygame.K_DOWN:
                print("Down key pressed")
                
        if event.type == pygame.KEYUP: #when we release the arrow keys
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Key released")
                playerX_change = 0

    player_x += playerX_change

    #Keeps our player in bounds
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    player(player_x,player_y)

    #We have to tell pygame to update the game screen with the changes that we've made
    pygame.display.update()