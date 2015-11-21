'''Talaba Pogrebinsky 1/14/2015'''
'''project 1d'''
import turtle
speed = input('''type the pen speed you would like: you can say:
slow, fast, fastest: ''')
turtle.speed(speed)
def draw_triangle(distance, angle):
    for i in range(3):
        turtle.forward(distance)
        turtle.left(angle)
def colored_triangle(distance, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    draw_triangle(distance, 120)
    turtle.end_fill()
    
uo_color = 'green'
x = 225
#adjusting position so spiral fits
turtle.penup()
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.pendown()
turtle.pensize(2)

#begining loop for spiral
for i in range(50):
    colored_triangle(x, uo_color)
    turtle.forward(18)
    turtle.right(7)
    x = x - 4
    if uo_color == 'green':
        uo_color = 'yellow' 
    else:
            uo_color = 'green'
#end

    
    

