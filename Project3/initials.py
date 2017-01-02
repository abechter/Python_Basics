import turtle

def move_left(pos):
	pos.color("white")
	pos.left(180)
	pos.forward(200)
	pos.right(180)

def draw_triangle(triangle):
	for i in range (1,4):
		triangle.right(120)
		triangle.forward(100)

def set_appearance(appearance):
	appearance.shape("turtle")
	appearance.color("green")

def letter_A(pen):
	pen.left(60)
	pen.forward(200)
	draw_triangle(pen)
	pen.right(120)
	pen.forward(200)

def letter_B(pen):
	pen.left(150)
	pen.forward(172)
	pen.right(180)
	pen.forward(172)
	pen.left(90)
	pen.circle(44,180)
	pen.right(180)
	pen.circle(42,180)

def main():
	window = turtle.Screen()
	window.bgcolor("white")

	ben = turtle.Turtle()

	move_left(ben)
	set_appearance(ben)
	letter_A(ben)
	letter_B(ben)
	
	window.exitonclick()

main ()
