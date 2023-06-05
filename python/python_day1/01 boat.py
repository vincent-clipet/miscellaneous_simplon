import turtle
import math 


turtle.color("red")

# Move to initial position
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()

# draw triangle
#turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)

turtle.penup()


# draw vertical line
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.setheading(90)
turtle.forward(math.sqrt(3)/2 * 200)

# draw bottom part
turtle.penup()
turtle.setheading(0)
turtle.goto(-100,-10)
turtle.pendown()
turtle.begin_fill()

turtle.forward(200)
# underwater_part_length = 200 * (math.sin(25)) / (2 * 50)
cos = math.cos(math.radians(25))
print(cos)
underwater_part_length = 200 - (50 * cos * 2)
turtle.right(155)
turtle.forward(50)
turtle.right(25)
turtle.forward(underwater_part_length)
turtle.right(25)
turtle.forward(50)
turtle.end_fill()

turtle.done()







turtle.done()
