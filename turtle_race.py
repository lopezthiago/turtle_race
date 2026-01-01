from turtle import Turtle, Screen, xcor, ycor
import random

screen = Screen()
screen.title("DATURTLE 500")

finish_line = [300, 300]
racers = []

class Racer(Turtle):
    def __init__(self, name, color, y_position):
        super().__init__()
        self.name = name
        self.shape('turtle')
        self.color(color)
        self.penup()
        self.goto(-400, y_position)
        racers.append(self)

def make_line():
    line = Turtle()
    line.penup()
    line.goto(300, 300)
    line.pendown()
    line.pensize(5)
    line.right(90)
    line.forward(600)
    line.penup()
    line.right(90)
    return line

def track_winner(line, winner):
    x_winner = int(winner.xcor() + 35)
    line.goto(x_winner, winner.ycor())


Racer("RED", "red", 0)
Racer("BLUE", "blue", -100)
Racer("GREEN", "green", 100)
Racer("YELLOW", "gold", 200)
Racer("PINK", "hot pink", -200)


while True:
    player_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? (red, blue, green, yellow, pink) ')
    if player_bet not in ['red', 'blue', 'green', 'yellow', 'pink']:
        print('Invalid bet! No bet placed.')
    else:
        break

line = make_line()

def start_race():
    global xcor, ycor
    racing = True
    winner = racers[0]
    track_winner(line, winner)

    while racing:

        for r in racers:
            r.forward(random.randint(1,15))

        for t in racers:

            if winner.xcor() < t.xcor():
                winner = t

            track_winner(line, winner)

            if t.xcor() > 290:
                racing = False
                
    for t in racers:
        if t != winner:
            t.hideturtle()
        else:
            print(f'{winner.name} TURTLE WINS!')
            if player_bet.lower() == winner.name.lower():
                print('You won the bet!')
            else:
                print('You lost the bet!')

start_race()

screen.exitonclick()
