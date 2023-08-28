import pygame


pygame.init()

screen_width = 1080
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("외로운 여행 - 1. 사막")

clock = pygame.time.Clock()


background = pygame.image.load("level1.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))
character = pygame.image.load("character.jpeg")

character_x_pos = 0
character_y_pos = 403

to_x = 0
to_y = 0


running = True
while running:
    dt = clock.tick(60)

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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - 35:
        character_x_pos = 1045

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > 403:
        character_y_pos = 403

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()
