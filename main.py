"""
Space Invaders in Python
Created by: Kati Baker for Code Camp 2023
"""
import pygame #tells our compiler (Visual Studio Code) to pull the pygame library into our Python file

#Initializes pygame library
pygame.init()

#Set the height and width of our game screen (width, height)
#(0,0) starts in our top left corner
screen = pygame.display.set_mode((600, 800))

#Set the title of our game screen
pygame.display.set_caption("Space Invaders at Code Camp 2023")

#Set the icon of our game screen
game_icon = pygame.image.load("assets/player/playerShip1_orange.png") #what's inside quotations has to match the path of where the image is
pygame.display.set_icon(game_icon)

#Setting the player icon
player_image = game_icon

#Player starting position
player_x = 250
player_y = 480

def player():
    screen.blit(player_image, (player_x, player_y))

"""
Game Logic
Summary: Logic to keep the game screen running until the player hits the close window button
"""
game_running = True
while game_running:
    #Game Logic to exit our game
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #this pygame.QUIT is referencing the pygame library
            game_running = False

    #Changes background color of the game screen using RGB (red, green, blue)
    screen.fill((0,0,0))

    player()
    #We have to tell pygame to update the game screen with the changes that we've made
    pygame.display.update()