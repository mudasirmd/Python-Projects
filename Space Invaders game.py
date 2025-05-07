import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Space Invaders")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Stops automatic updates

# Player spaceship
player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()
player.goto(0, -250)
player.setheading(90)  # Pointing upwards
player.speed(0)

# Bullet
bullet = turtle.Turtle()
bullet.shape("square")
bullet.color("yellow")
bullet.penup()
bullet.speed(0)
bullet.hideturtle()
bullet.setheading(90)
bullet.speed(10)
bullet_state = "ready"  # "ready" or "fire"


# Player movement functions
def move_left():
    x = player.xcor()
    if x > -350:
        player.setx(x - 20)


def move_right():
    x = player.xcor()
    if x < 350:
        player.setx(x + 20)


def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()


# Keyboard bindings
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(fire_bullet, "space")

# Alien setup
aliens = []
alien_speed = 2
for i in range(5):
    for j in range(6):
        alien = turtle.Turtle()
        alien.shape("square")
        alien.color("green")
        alien.penup()
        alien.goto(-250 + (i * 100), 250 - (j * 50))
        aliens.append(alien)

# Barrier setup
barriers = []
for i in range(3):
    barrier = turtle.Turtle()
    barrier.shape("square")
    barrier.color("blue")
    barrier.penup()
    barrier.goto(-200 + (i * 200), -100)
    barriers.append(barrier)


# Collision detection
def is_collision(t1, t2):
    if t1.distance(t2) < 20:
        return True
    return False


# Main game loop
game_over = False
while not game_over:
    screen.update()

    # Move the aliens down
    for alien in aliens:
        y = alien.ycor()
        alien.sety(y - alien_speed)

        # Check for collision with player
        if is_collision(player, alien):
            game_over = True
            print("Game Over! You were hit by an alien.")
            break

        # Check for alien reaching the bottom
        if alien.ycor() < -250:
            game_over = True
            print("Game Over! Aliens reached the player.")
            break

    # Move the bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        bullet.sety(y + 20)

        # Check if bullet hits an alien
        for alien in aliens:
            if is_collision(bullet, alien):
                bullet.hideturtle()
                bullet_state = "ready"
                alien.goto(random.randint(-350, 350), random.randint(100, 250))
                break

        # If bullet reaches the top, reset it
        if bullet.ycor() > 290:
            bullet.hideturtle()
            bullet_state = "ready"

    # Alien movement towards player
    if random.random() < 0.02:  # Randomly make aliens shoot
        alien_shooter = random.choice(aliens)
        bullet_alien = turtle.Turtle()
        bullet_alien.shape("square")
        bullet_alien.color("red")
        bullet_alien.penup()
        bullet_alien.goto(alien_shooter.xcor(), alien_shooter.ycor() - 20)
        bullet_alien.setheading(270)
        bullet_alien.speed(10)

        while bullet_alien.ycor() > -290:
            bullet_alien.sety(bullet_alien.ycor() - 10)
            screen.update()
            if is_collision(bullet_alien, player):
                game_over = True
                print("Game Over! You were hit by an alien bullet.")
                break

    time.sleep(0.02)  # Slow down the game loop

# End game message
screen.clear()
game_end = turtle.Turtle()
game_end.color("red")
game_end.penup()
game_end.hideturtle()
game_end.goto(0, 0)
game_end.write("Game Over", align="center", font=("Arial", 24, "bold"))

screen.mainloop()
