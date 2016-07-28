'Talaba Pogrebinsky 01/15/2015 project 1c.'

import turtle
#triangle
def draw_triangle(distance, angle):
    for i in range(3):
        turtle.forward(distance)
        turtle.left(angle)

def colored_triangle(distance, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    draw_triangle(distance, 120)
    turtle.end_fill()

def color_circle(radius, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

#triangle
for i in range(1):
    colored_triangle(100, 'blue')

    

        


turtle.penup()
turtle.forward(-10)
turtle.left(90)

#square
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('green')
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()

turtle.left(90)
turtle.left(90)
turtle.penup()
turtle.forward(150)


#square2
turtle.begin_fill()
turtle.fillcolor('orange')
turtle.pendown()
turtle.pencolor('blue')
turtle.pensize(3)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
 
 

turtle.right(90)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.end_fill()
#circle1
turtle.begin_fill()
turtle.fillcolor('purple')
turtle.circle(50)
turtle.penup()
turtle.forward(130)
turtle.end_fill()

#circle2
turtle.pendown()
turtle.pencolor('blue')
turtle.pensize(3)
for i in range(1):
    color_circle(50, 'yellow')
    

    
    
