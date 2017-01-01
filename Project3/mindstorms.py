import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()

	brad.color("green")
	brad.shape("turtle")
	brad.speed(3)

	
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)

	window.exitonclick()

draw_square()
