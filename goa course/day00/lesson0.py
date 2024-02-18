from turtle import *

speed(30)
#we wont to paint a hous
#step 1:  draw a square
width(7)
forward(200)
left(90)
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(15, 130)
right(150)
pendown()
forward(60)
right(90)
forward(50)
right(90) 
forward(60)  
right(90)
forward(50)

penup()
goto(180,130)
pendown()
forward(50)
right(90)
forward(60)
right(90)
forward(50)
right(90)
forward(60)


exitonclick()