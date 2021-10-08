#Download turtle to be able to use it.
import turtle

#Creates the playground for turtle
wn = turtle.Screen()

#Set the window background color
wn.bgcolor('#CBC3E3')

#Set the window title
wn.title('Draw a Square and a Triangle')

#Assign a variable to my turtle
morla = turtle.Turtle()

#Assign color and size to turtle
morla.color('#1c162f')
morla.pensize(3)

#Draw a square
for s in [0, 1, 2, 3]:
    morla.forward(150)
    morla.left(90)

#Draw a triangle
for t in [0, 1, 2]:
    morla.backward(150)
    morla.right(120)


#Keeps the window open until it is closed out
wn.mainloop()

