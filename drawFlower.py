import turtle

def draw_square(turtle):
	for i in range(4):
		turtle.forward(120)
		turtle.right(90)

window=turtle.Screen()

kim=turtle.Turtle()
kim.speed(30)
kim.color("blue")

kim.right(90)
for i in range(72):
	draw_square(kim)
	kim.right(5)

kim.width(5)
kim.forward(250)
window.exitonclick()

