import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(127, 173, 198), (222, 219, 210), (179, 174, 160), (197, 209, 215), (25, 22, 8), (112, 108, 67), (7, 32, 39), (65, 113, 127), (198, 193, 181), (164, 200, 214), (143, 141, 87), (219, 225, 223), 
(80, 79, 27), (8, 14, 12), (156, 165, 163), (91, 140, 156), (93, 106, 101), (23, 80, 93), (238, 235, 237), (184, 195, 194), (26, 20, 22), (116, 134, 129), (87, 55, 45), (42, 75, 70), (143, 122, 
115), (89, 77, 80), (168, 162, 164), (186, 192, 199), (205, 187, 180), (97, 133, 159)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()

