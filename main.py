from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
# bittu=Turtle()
screen=Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake=Snake()
food=Food()
scoreb=Scoreboard()
game=True
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')
while game:
    screen.update()
    time.sleep(.2)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        scoreb.score()
        snake.extend()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreb.game_over()
        game=False
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreb.game_over()
            game=False



























screen.exitonclick()

