# Import Modules 
import turtle
import time
import random

delay = 0.1

# Score
score = 0

# Set up the screen
screen = turtle.Screen()
screen.title("Snake")
# Set Background to dark Color
screen.bgcolor("#2e3440")
# Set window Size
screen.setup(width=600, height=600)
screen.tracer(0) 

# Draw border around screen
border = turtle.Turtle()
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.forward(600)
    border.left(90)
border.hideturtle()


# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#5e81ac")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Food (Apples)
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("#bf616a")
food.penup()
food.goto(0,100)

# Snake Body List
segments = []

# Score pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Move Snake On wsad keys
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

# Main game loop
while True:
    screen.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        # Write The Score 
        pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal")) 


    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random area
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#d08770")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10   

        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            # wait one second before restarting
            time.sleep(1)
            # reset position
            head.goto(0,0)
            head.direction = "stop"
        
            # hide the tail
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Remove all segments from segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

screen.mainloop()
