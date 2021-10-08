#Download turtle to be able to use it.
import turtle

wn = turtle.Screen()

#Set the window background color
wn.bgcolor('pink')

#Set the window title
wn.title('Draw First and Last Initial')

#Assign a variable to my turtle
morla = turtle.Turtle()

#Assign color and size to turtle
morla.color('#1c162f')
morla.pensize(2)

#Turn the pen to face new direction
morla.left(180)

#Raises the pen so I can move turtle
morla.penup()

#Move turtle to left side of the screen
morla.forward(300)
morla.left(90)
morla.forward(200)
morla.right(180)

#Put the pen down
morla.pendown()

#Start the first initial
morla.forward(360)
morla.right(90)
morla.forward(90)
morla.circle(-90, 180)
morla.forward(90)
morla.right(180)
morla.forward(90)
morla.circle(-90, 180)
morla.forward(90)

#Move turtle to new location
morla.penup()
morla.left(180)
morla.forward(300)

#Start the last initial
morla.left(90)
morla.pendown()
morla.forward(360)
morla.right(90)
morla.forward(90)
morla.circle(-90, 180)
morla.forward(90)
morla.right(180)
morla.forward(90)
morla.circle(-90, 180)
morla.forward(90)

#Keep screen open until window closed
wn.mainloop()
