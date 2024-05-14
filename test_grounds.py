import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('fish.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480


def player(x, y):
    screen.blit(playerImg, (x, y))


running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX -= 10
                print("Left arrow is pressed")

            elif event.key == pygame.K_RIGHT:
                playerX += 10
                print("Right arrow is pressed")

            elif event.key == pygame.K_UP:
                playerY -= 10
                print("up arrow is pressed")

            elif event.key == pygame.K_DOWN:
                playerY += 10
                print("down arrow is pressed")

    player(playerX, playerY)
    pygame.display.update()