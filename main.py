import pygame
import random
pygame.init()
pygame.font.init()

win = pygame.display.set_mode((600, 600))

DICE_1 = pygame.image.load("1.jpg")
DICE_2 = pygame.image.load("2.jpg")
DICE_3 = pygame.image.load("3.jpg")
DICE_4 = pygame.image.load("4.jpg")
DICE_5 = pygame.image.load("5.jpg")
DICE_6 = pygame.image.load("6.jpg")

dice_choice = 1
if dice_choice == 1:
    win.blit(DICE_1, (300, 250))
    pygame.display.update()

if dice_choice == 2:
    win.blit(DICE_2, (400, 100))
    pygame.display.update()

if dice_choice == 3:
    win.blit(DICE_3, (300, 300))
    pygame.display.update()

if dice_choice == 4:
    win.blit(DICE_4, (300, 300))
    pygame.display.update()

if dice_choice == 5:
    win.blit(DICE_5, (300, 300))
    pygame.display.update()

if dice_choice == 6:
    win.blit(DICE_6, (300, 300))
    pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False