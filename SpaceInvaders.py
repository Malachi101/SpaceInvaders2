import pygame

 # Initalize the pygame
pygame.init()

 # Create the screen
screen = pygame.display.set_mode((800,600))

 # Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('')
pygame.display.set_icon(icon)

 # Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))

# Game Loop
running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            runnning = False

    player()
    pygame.display.update()

    #