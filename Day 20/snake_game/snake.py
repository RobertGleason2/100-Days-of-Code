from turtle import Turtle

# Constants
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# TODO: Create Snake Body
# Turtle dimensions are 20x20
# TODO: Move the snake


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        

    def create_snake(self):
        for seg_index in STARTING_POSITIONS:
            self.add_segment(seg_index)


    def add_segment(self, position):
            snake_segment = Turtle(shape="square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(position)
            self.segments.append(snake_segment)

    def extend(self):
        # add a new segemnt to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        # loop through each segement in reverse order
        # used to move the snake forward
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_y = self.segments[seg_num-1].ycor()
            new_x = self.segments[seg_num-1].xcor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)