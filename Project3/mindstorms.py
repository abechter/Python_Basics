import turtle

def draw_square(some_turtle):
	
	some_turtle.color("green")
	some_turtle.shape("turtle")
	some_turtle.speed(3)

	i = 0
	while (i < 4): 
		some_turtle.forward(100)
		some_turtle.right(90)
		i = i + 1

def draw_circle():
	angie = turtle.Turtle()
	
	angie.color("blue")
	angie.shape("arrow")
	angie.circle(50)

def draw_triangle():
	marc = turtle.Turtle()

	marc.color("yellow")
	marc.shape("circle")
	
	marc.forward(100)
	marc.right(120)
	marc.forward(100)
	marc.right(120)
	marc.forward(100)


def main():
        window = turtle.Screen()
        window.bgcolor("red")
        brad = turtle.Turtle()

        draw_square(brad)
        draw_circle()
        draw_triangle()

        for a in range (1,37):
                draw_square(brad)
                brad.right(10)

        window.exitonclick()


main()
