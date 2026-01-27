# import colorgram
import turtle as t
import random
# colors = colorgram.extract('image.jpg', 30)

# uses the package colorgram to get a list of tuples of colors from the image
# Used to get the colors for the list
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

t.colormode(255)

color_list = [ (211, 154, 97), (52, 108, 132), (236, 245, 241), (177, 78, 33), (198, 143, 35), (117, 154, 170), (124, 79, 98), (122, 175, 158), (234, 239, 243), (229, 196, 128), (192, 86, 107), (55, 39, 20), (11, 51, 64), (193, 123, 142), (54, 121, 116), (41, 168, 127), (167, 21, 30), (225, 94, 79), (38, 31, 33), (5, 28, 26), (243, 164, 160), (80, 149, 171), (163, 26, 22), (235, 166, 171), (105, 124, 159), (23, 79, 90), (171, 207, 189), (158, 205, 214)]


timmy = t.Turtle()
timmy.speed("fastest")
screen = t.Screen()

timmy.penup()
timmy.hideturtle()

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count%10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = t.Screen()
screen.exitonclick()