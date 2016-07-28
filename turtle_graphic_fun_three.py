"Talaba Pogrebinsky project 1e 01/14/2015"
import turtle

def draw_tree(trunk_color, leaf_color):
    turtle.begin_fill()
    turtle.fillcolor(trunk_color)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(15)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(32)
    turtle.right(65)
    
    
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(leaf_color)
    turtle.circle(20)
    turtle.end_fill()
    
#end def
print("Hello!, im going to draw you a picture!")

print('what speed would you like me to draw?')

turtle.speed = input(" you can type: slow, fast, or fastest: ")
    
trunk_color = input(" okay, what color tree trunks would you like? ")
leaf_color  = input(" okay, what color leaves would you like? ")
bldg_color  = input(" okay, what color buildings would you like? ")
roof_color  = bldg_color


def draw_building():
    #first square
    turtle.begin_fill()
    turtle.fillcolor(bldg_color)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.end_fill()
    turtle.left(180)
    turtle.forward(50)
    turtle.left(90)
    #first half of roof
    turtle.begin_fill()
    turtle.fillcolor(roof_color)
    turtle.right(135)
    turtle.forward(35)
    turtle.right(90)
    turtle.forward(35)
    turtle.right(135)
    turtle.forward(50)
    turtle.end_fill()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    #second square
    
    turtle.left(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(50)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(50)
  
    turtle.begin_fill()
    turtle.fillcolor(bldg_color)
    #third square
    turtle.left(90)
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(50)
    turtle.end_fill()
    #second half of roof
    turtle.begin_fill()
    turtle.fillcolor(roof_color)
    turtle.right(45)
    turtle.forward(35)
    turtle.right(90)
    turtle.forward(35)
    turtle.right(135)
    turtle.forward(50)
    turtle.right(90)
    turtle.end_fill()
    #end def

    #Moving in between and using defs.
#building
draw_building()
turtle.penup()
turtle.forward(100)
turtle.right(90)
turtle.pendown()
#tree
draw_tree(trunk_color, leaf_color)
turtle.penup()
turtle.right(135)
turtle.forward(90)
turtle.pendown()
turtle.left(110)
#tree
draw_tree(trunk_color, leaf_color)
turtle.penup()
turtle.forward(50)
turtle.right(45)
turtle.forward(100)
turtle.pendown()
turtle.left(20)
#building
turtle.pencolor('black')

draw_building()
turtle.right(180)
turtle.penup()
turtle.forward(400)
#building
turtle.pendown()
turtle.left(90)
draw_building()
turtle.penup()
turtle.forward(100)
turtle.right(90)

#building
turtle.pencolor('black')
turtle.left(180)
turtle.forward(225)
turtle.left(90)
turtle.forward(200)
turtle.right(270)
turtle.pendown()
draw_building()
turtle.penup()
turtle.forward(100)
turtle.right(90)
turtle.pendown()
#tree

draw_tree(trunk_color, leaf_color)
turtle.penup()
turtle.forward(50)
turtle.right(45)
turtle.forward(100)
turtle.pendown()
turtle.right(80)
#tree
turtle.left(100)
draw_tree(trunk_color, leaf_color)
turtle.penup()
turtle.forward(50)
turtle.right(45)
turtle.forward(100)
turtle.pendown()
#tree
turtle.left(20)

draw_tree(trunk_color, leaf_color)
turtle.penup()
turtle.forward(50)
turtle.right(45)
turtle.forward(100)
turtle.pendown()
turtle.right(80)






    
