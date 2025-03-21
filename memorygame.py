from random import shuffle
from turtle import *
from freegames import path

car = path('car.gif')
characters = list("ABCDEFGHJKLMNOPQRSTUVWXYZ@#$%&*+!?")
tiles = characters * 2
state = {'mark': None, "taps": 0}
hide = [True] * 64

def square(x, y):
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for _ in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def juego_terminado():
    return all(not escondido for escondido in hide)

def tap(x, y):
    spot = index(x, y)
    mark = state['mark']

    state["taps"] += 1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 15, y + 5)
        color('black')
        write(tiles[mark], align="center", font=('Arial', 30, 'normal'))

    up()
    goto(0, 200)
    color("black")
    write(f"Taps: {state['taps']}", align="center", font=('Arial', 14, 'normal'))

    if juego_terminado():
        goto(0, 0)
        color("green")
        write("¡Ganaste!", align="center", font=('Arial', 20, 'bold'))
    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
