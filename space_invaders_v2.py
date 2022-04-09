#classic space  invaders
import turtle
import os
import math
import random

#setting up the screen
win = turtle.Screen()
win.bgcolor("black")
win.title("Space Invaders :)")
win.bgpic("space_invaders_background.gif")

#registering shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

#drawing a border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-250, -250)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(500)
    border_pen.lt(90)
    border_pen.hideturtle()

score = 0 #initial score
score_pen = turtle.Turtle()
score_pen2 = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-250, 270)
score_string = "Score : %s" % score
holo = "- Aditya Panchal"
score_pen.write(score_string, False, align = "left", font = ("Courier New", 14, "normal"))
score_pen.penup()
score_pen2.speed(0)
score_pen2.color("white")
score_pen2.penup()
score_pen2.setposition(250, -270)
score_pen2.write(holo, False, align = "right", font = ("Courier New", 8, "normal"))
score_pen2.hideturtle()

#creating player Turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -200)
player.setheading(90)

playerspeed = 15

#creating a list of invaders
enemies = []
enemyspeed = 1.5
i = 12

def create_enemies(i):
	y = 230
	prev = -210
	flag = prev
	for count in range(i):
	    enemies.append(turtle.Turtle())
	for enemy in enemies:
	    enemy.color("red")
	    enemy.shape("invader.gif")
	    enemy.speed(0)
	    enemy.penup()
	    x = prev + 50
	    prev = x
	    if(x > 150):
	    	x = flag + 50
	    	prev = x
	    	y -= 30
	    enemy.setposition(x, y)

#creating player's bullet
#bullet = turtle.Turtle()
#bullet.color("red")
#bullet.shape("circle")
#bullet.speed(0)
#bullet.penup()
#bullet.shapesize(0.4, 0.4)
#bullet.setposition(0, -250)
#bullet.hideturtle()
#bulletstate = "ready" #ready to fire

#moving the player left and right and bullet
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -230: #boundary check
        x = -230
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 230: #boundary check
        x = 230
    player.setx(x)

bullets = []
bulletspeed = 40

def fire_bullet():
	bullet = turtle.Turtle()
	bullet.hideturtle()
	bullet.color("red")
	bullet.shape("circle")
	bullet.speed(0)
	bullet.penup()
	bullet.shapesize(0.4, 0.4)
	bullet.setposition(player.xcor(), player.ycor() + 10)
	bullet.showturtle()
	bullets.append(bullet)

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 23:
        return True
    else:
        return False

#creating keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

flag = 0

create_enemies(i)

#main game loop
while True:
    for enemy in enemies:
        #moving enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        #boundary check and reverse down
        if enemy.xcor() > 230:
            for e in enemies:
                y = e.ycor()
                y -= 30
                e.sety(y)
            enemyspeed *= -1.05
        if enemy.xcor() < -230:
            for e in enemies:
                y = e.ycor()
                y -= 30
                e.sety(y)
            enemyspeed *= -1.05
        #checking for bullet collision
        for bullet in bullets:
            if isCollision(bullet, enemy):
                enemy.hideturtle()
                enemies.remove(enemy)
                #resetting bullet
                bullet.hideturtle()
                bullets.remove(bullet)
                #bulletstate = "ready"
                #bullet.setposition(0, -400)
                #resetting invader
                #x = random.randint(-170, 170)
                #enemy.setposition(x, 230)
                #updating score
                score += 1
                score_string = "Score : %s" % score
                score_pen.clear()
                score_pen.write(score_string, False, align = "left", font = ("Courier New", 14, "normal"))
                score_pen.hideturtle()

        if isCollision(player, enemy):
            flag = 1
            break

        if enemy.ycor() <= player.ycor():
            flag = 1
            break

    if enemies == []:
    	i += 1 
    	create_enemies(i)

    if flag == 1:
        print("Game Over!")
        player.hideturtle()
        bullet.hideturtle()
        for enemy in enemies:
            enemy.hideturtle()
            score_pen = turtle.Turtle()
            score_pen.speed(0)
            score_pen.color("white")
            score_pen.penup()
            score_string = "Final Score : %s" % score
            score_pen.write(score_string, False, align = "center", font = ("Courier New", 18, "bold"))
        break

    #moving the bullet
    for bullet in bullets:
    	y = bullet.ycor();
    	y += bulletspeed
    	bullet.sety(y)
    	#checking if bullet has reached the top
    	if bullet.ycor() > 250:
        	#bulletstate = "ready"
        	bullet.hideturtle()
        	bullets.remove(bullet)

delay = input("Press enter to exit.")
