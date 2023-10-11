"""
This is snake game developed in python language with pygame library by Arth.
"""

import random

import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))

snake = [(100, 100)]
food = (random.randint(0, 590), random.randint(0, 390))
snake_direction = (0, 1)
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake_direction = (1, 0)

    snake.insert(0, (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1]))
    snake.pop()

    if snake[0] == food:
        snake.append((snake[-1][0] + snake[-1][1], snake[-1][1]))

        food = (random.randint(0, 590), random.randint(0, 390))
    if snake[0] in snake[1:] or snake[0][0] < 0 or snake[0][0] > 590 or snake[0][1] < 0 or snake[0][1] > 390:
        running = False

    screen.fill((0, 0, 100))
    for segment in snake:
        pygame.draw.rect(screen, (255, 255, 255), (segment[0], segment[1], 10, 10))

    pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], 10, 10))
    pygame.display.update()
    pygame.time.Clock().tick(100)

pygame.quit()
