from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboardpong import Scoreboard



screen=Screen()
screen.setup(800,600)
screen.bgcolor('black')
screen.title('My Pong Game')
screen.tracer(0)

r_paddle=Paddle(350)
l_paddle=Paddle(-350)
pong=Ball()
score=Scoreboard()
screen.listen()
screen.onkey(r_paddle.up,'Up')
screen.onkey(r_paddle.down,'Down')
screen.onkey(l_paddle.up,'w')
screen.onkey(l_paddle.down,'s')
game_is_on=True
lapse=.1
while game_is_on:
    time.sleep(lapse)
    screen.update()
    pong.start()
    if pong.ycor()>280 or pong.ycor()<-280:
        pong.reflect_s()
    if pong.distance(l_paddle)<50 and pong.xcor()<-320 or pong.distance(r_paddle)<50 and pong.xcor()>320 :
        pong.reflect_p()
        lapse/=2
        time.sleep(lapse)
    if pong.xcor()>380:
        pong.goto(0,0)
        pong.reflect_p()
        score.r_wins()
    if pong.xcor()<-380:
        pong.goto(0,0)
        pong.reflect_p()
        score.l_wins()









screen.exitonclick()

