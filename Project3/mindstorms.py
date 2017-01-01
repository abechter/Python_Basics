import turtle

def draw_square():
	brad = turtle.Turtle()

	brad.color("green")
	brad.shape("turtle")
	brad.speed(3)

	i = 0
	while (i < 4): 
		brad.forward(100)
		brad.right(90)
		i = i + 1

def draw_circle():
	angie = turtle.Turtle()
	
	angie.color("blue")
	angie.shape("arrow")
	angie.circle(50)


def main():
        window = turtle.Screen()
        window.bgcolor("red")

        draw_square()
        draw_circle()

        window.exitonclick()


main()
