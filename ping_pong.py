#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pygame')


# In[7]:


import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Window parameters
WIDTH, HEIGHT = 600, 400
BALL_RADIUS = 15
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 60
FPS = 60

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Initialize the ball
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)
ball_speed = [5, 5]

# Initialize paddles
paddle_left = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_right = pygame.Rect(WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Score counters
score_left = 0
score_right = 0

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    # Left paddle control
    if keys[pygame.K_w] and paddle_left.top > 0:
        paddle_left.y -= 5
    if keys[pygame.K_s] and paddle_left.bottom < HEIGHT:
        paddle_left.y += 5

    # Right paddle control
    if keys[pygame.K_UP] and paddle_right.top > 0:
        paddle_right.y -= 5
    if keys[pygame.K_DOWN] and paddle_right.bottom < HEIGHT:
        paddle_right.y += 5

    # Update the ball's position
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Bounce the ball off the top and bottom boundaries
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Bounce the ball off the paddles
    if ball.colliderect(paddle_left) or ball.colliderect(paddle_right):
        ball_speed[0] = -ball_speed[0]

    # Check if the ball goes out of bounds horizontally (scoring)
    if ball.left <= 0:
        # Return the ball to the center
        ball.x = WIDTH // 2 - BALL_RADIUS // 2
        ball.y = HEIGHT // 2 - BALL_RADIUS // 2
        # Change the ball's direction
        ball_speed[0] = -ball_speed[0]
        # Increase the score for the right player
        score_right += 1

    if ball.right >= WIDTH:
        # Return the ball to the center
        ball.x = WIDTH // 2 - BALL_RADIUS // 2
        ball.y = HEIGHT // 2 - BALL_RADIUS // 2
        # Change the ball's direction
        ball_speed[0] = -ball_speed[0]
        # Increase the score for the left player
        score_left += 1

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw paddles and the ball
    pygame.draw.rect(screen, (255, 255, 255), paddle_left)
    pygame.draw.rect(screen, (255, 255, 255), paddle_right)

    # Set a random color for the ball
    ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.ellipse(screen, ball_color, ball)

    # Draw the score display
    font = pygame.font.Font(None, 36)
    score_display = font.render(f"{score_left} - {score_right}", True, (255, 255, 255))
    screen.blit(score_display, (WIDTH // 2 - score_display.get_width() // 2, 10))

    # Update the screen
    pygame.display.flip()

    # Delay to control the game's speed
    clock.tick(FPS)


# In[ ]:




