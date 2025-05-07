import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
BALL_RADIUS = 10
BRICK_WIDTH = 60
BRICK_HEIGHT = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout Game")

# Clock
clock = pygame.time.Clock()

# Paddle class
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 10

    def move(self, x_change):
        if self.rect.left + x_change >= 0 and self.rect.right + x_change <= SCREEN_WIDTH:
            self.rect.x += x_change

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

# Ball class
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.dx = 4
        self.dy = -4

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def draw(self):
        pygame.draw.circle(screen, WHITE, self.rect.center, BALL_RADIUS)

    def bounce(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.dy = -self.dy
            self.rect.y = paddle.rect.top - BALL_RADIUS  # reset ball position above paddle

# Brick class
class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)

# Game function
def game():
    paddle = Paddle(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 50)
    ball = Ball(SCREEN_WIDTH // 2 - BALL_RADIUS, SCREEN_HEIGHT - 70)
    
    bricks = []
    for i in range(5):
        for j in range(10):
            brick = Brick(j * (BRICK_WIDTH + 10) + 35, i * (BRICK_HEIGHT + 5) + 35)
            bricks.append(brick)

    score = 0
    running = True
    while running:
        screen.fill(BLACK)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move(-paddle.speed)
        if keys[pygame.K_RIGHT]:
            paddle.move(paddle.speed)

        # Move ball
        ball.move()

        # Ball collisions
        if ball.rect.left <= 0 or ball.rect.right >= SCREEN_WIDTH:
            ball.dx = -ball.dx
        if ball.rect.top <= 0:
            ball.dy = -ball.dy
        if ball.rect.bottom >= SCREEN_HEIGHT:
            running = False  # Game over
        
        # Ball collision with bricks
        for brick in bricks[:]:
            if ball.rect.colliderect(brick.rect):
                bricks.remove(brick)
                ball.dy = -ball.dy
                score += 1

        # Draw everything
        paddle.draw()
        ball.draw()
        for brick in bricks:
            brick.draw()

        # Draw score
        font = pygame.font.SysFont('Arial', 24)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update display
        pygame.display.flip()
        
        # Set FPS
        clock.tick(60)

# Run the game
game()

# Quit pygame
pygame.quit()
