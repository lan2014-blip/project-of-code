import turtle

turtle.Screen().bgcolor("aqua")
turtle.Screen().setup(400,600)

triangle=turtle.Turtle()

length=100
angle=120

for i in range(4):
    triangle.forward(length)
    triangle.right(angle)

length=100
angle=118

for i in range(4):
    triangle.forward(length)
    triangle.right(angle)

turtle.done()