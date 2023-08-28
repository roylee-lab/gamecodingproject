import pygame
import random


pygame.init()

screen_width = 1080
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Cosmic Adventure -코즈믹 어드벤처")

clock = pygame.time.Clock()


character = pygame.image.load("character.png")
character_left = pygame.image.load("character_left.png")
character_right = pygame.image.load("character_right.png")
character_jump_left = pygame.image.load("character_jump_left.png")
character_jump_right = pygame.image.load("character_jump_right.png")


character_x_pos = 0
character_y_pos = 330

to_x = 0
to_y = 0

level = 1

running = True
while running:
    dt = clock.tick(60)

    if level == 1:
        background = pygame.image.load("level1.jpg")

        screen.blit(background, (0, 0))

    if level == 2:
        background = pygame.image.load("level2.jpg")

        screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
            elif event.key == pygame.K_SPACE:
                to_x = 100
                to_y = 100

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - 100:
        character_x_pos = 980

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > 330:
        character_y_pos = 330

    if character_x_pos == 325 and character_y_pos == 975:
        print("Game Cleared!!")
        running = False

    screen.blit(character, (character_x_pos, character_y_pos))

    # block = Blocks(random.randint(1, 1010), random.randint(1, 410), "block.png", 10)
    # block.generate()

    pygame.display.update()

pygame.quit()
