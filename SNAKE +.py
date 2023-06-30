import pygame 
import time
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the font for displaying the score
font = pygame.font.Font(None, 36)

# Set up the initial position and size of the snake
snake_block_size = 20
snake_speed = 11
snake_x, snake_y = width // 2, height // 2
snake_x_change, snake_y_change = 0, 0
snake_body = []
snake_length = 1

# Set up the initial position of the food
food_x = round(random.randrange(0, width - snake_block_size) / 20) * 20
food_y = round(random.randrange(0, height - snake_block_size) / 20) * 20

# Game over flag
game_over = False

# Function to display the score on the screen
def show_score(score):
    score_text = font.render("Score: " + str(score), True, BLACK)
    display.blit(score_text, [10, 10])

# Function to display the game over screen
def game_over_screen(score):
    while True:
        display.fill(GREEN)
        game_over_text = font.render("Game Over", True, BLACK)
        score_text = font.render("Score: " + str(score), True, BLACK)
        restart_text = font.render("Press R to restart", True, BLACK)
        display.blit(game_over_text, [width // 2 - game_over_text.get_width() // 2, height // 2 - game_over_text.get_height() // 2 - 30])
        display.blit(score_text, [width // 2 - score_text.get_width() // 2, height // 2 - score_text.get_height() // 2])
        display.blit(restart_text, [width // 2 - restart_text.get_width() // 2, height // 2 - restart_text.get_height() // 2 + 30])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return  # Exit the game_over_screen function and restart the game

# Function to restart the game
def restart_game():
    global snake_x, snake_y, snake_x_change, snake_y_change, snake_body, snake_length, food_x, food_y, game_over
    snake_x, snake_y = width // 2, height // 2
    snake_x_change, snake_y_change = 0, 0
    snake_body = []
    snake_length = 1
    food_x = round(random.randrange(0, width - snake_block_size) / 20) * 20
    food_y = round(random.randrange(0, height - snake_block_size) / 20) * 20
    game_over = False

# Game loop
while not game_over:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_block_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_block_size
                snake_x_change = 0

    # Update snake position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for collisions with the boundaries of the window
    if snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height:
        game_over_screen(snake_length - 1)

    # Check for collision with the food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, width - snake_block_size) / 20) * 20
        food_y = round(random.randrange(0, height - snake_block_size) / 20) * 20
        snake_length += 1

    # Update the display
    display.fill(GREEN)
    pygame.draw.rect(display, RED, [food_x, food_y, snake_block_size, snake_block_size])
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_body.append(snake_head)
    if len(snake_body) > snake_length:
        del snake_body[0]
    for body_part in snake_body[:-1]:
        if body_part == snake_head:
            game_over_screen(snake_length - 1)
    for body_part in snake_body:
        pygame.draw.rect(display, BLACK, [body_part[0], body_part[1], snake_block_size, snake_block_size])
    show_score(snake_length - 1)
    pygame.display.update()

    # Set the speed of the game
    clock.tick(snake_speed)

    # Restart the game if the player presses the "R" key
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        restart_game()

# Quit Pygame
pygame.quit()
