from turtle import Screen, Turtle

pantalla = Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)

tortuga = Turtle()

tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)

tortuga.penup()
tortuga.right(90)
tortuga.forward(100)
tortuga.pendown()
tortuga.pensize(5)
tortuga.pencolor('orange')

tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)

tortuga.penup()
tortuga.forward(30)
tortuga.pendown()
tortuga.circle(10)

pantalla.exitonclick()