import turtle
wn = turtle.Screen()
north = turtle.Turtle()
wn.bgcolor("#d6ecef")
#Set the window title
wn.title('Draw a Snowflake')
north.pensize(2)

#Move turtle to different part of screen
north.penup()
north.left(180)
north.forward(100)
north.left(90)
north.forward(100)
north.left(180)
north.pendown()

# draw a N sided polygon
for i in range(0, 8):
    north.forward(50)
    north.backward(25)
    north.right(45)
    north.forward(25)
    north.backward(25)
    north.left(90)
    north.forward(25)
    north.backward(25)
    north.right(45)
    north.backward(25)
    north.right(45)

#Move turtle to another part of the screen
north.penup()
north.forward(200)
north.right(90)
north.forward(200)
north.pendown()

# draw a new N sided polygon
for i in range(0, 8):
    #Start line 1
    north.forward(100)
    #First set of flakes
    north.backward(25)
    north.right(45)
    north.forward(25)
    north.backward(25)
    north.left(90)
    north.forward(25)
    north.backward(25)
    north.right(45)
    #Second set of flakes
    north.backward(25)
    north.right(45)
    north.forward(25)
    north.backward(25)
    north.left(90)
    north.forward(25)
    north.backward(25)
    north.right(45)
    #Third set of flakes
    north.backward(25)
    north.right(45)
    north.forward(25)
    north.backward(25)
    north.left(90)
    north.forward(25)
    north.backward(25)
    north.right(45)
    #base of flake to move to next line
    north.backward(25)
    north.right(45)
    north.forward(25)
    north.right(120)
    north.forward(25)
    north.left(120)
   
#Keep screen open until window closed
wn.mainloop()
