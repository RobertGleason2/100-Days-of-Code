from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SSSnake SSSimulator")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(key= "Up", fun= snake.up)
screen.onkey(key= "Down", fun= snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food 
    if snake.head.distance(food) < 15:
        # Food go to a new random location
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    # give everything in the list except the first item
    for segement in snake.segments[1:]:
        if snake.head.distance(segement) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()