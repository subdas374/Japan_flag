import turtle

# 1. Setup the display canvas
screen = turtle.Screen()
screen.title("Coding Country Flags: Japan")
screen.setup(width=700, height=500)
screen.bgcolor("#1A1A1A") # Dark background makes the white flag pop on screen

t = turtle.Turtle()
t.speed(3) # Perfect speed for a satisfying video trace
t.pensize(2)

# 2. Draw the White Base Rectangle (Ratio 2:3)
t.penup()
t.goto(-225, 150) # Move to top-left corner
t.pendown()

t.color("#FFFFFF") # Pure White
t.begin_fill()
for _ in range(2):
    t.forward(450) # Width
    t.right(90)
    t.forward(300) # Height
    t.right(90)
t.end_fill()

# 3. Draw the Red Disc (Hinomaru) right in the center
# To make a circle perfectly centered, we move below the center point 
# because turtle draws circles upwards from its starting point.
t.penup()
t.goto(0, -90) # Center is (0,0), radius is 90, so we drop down to -90
t.pendown()

t.color("#BC002D") # Crimson Red (Official Japanese Flag Crimson)
t.begin_fill()
t.circle(90) # Draw the sun disk
t.end_fill()

# 4. Finish and hold screen
t.hideturtle()
screen.exitonclick()
