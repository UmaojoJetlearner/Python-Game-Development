import pgzrun
import random

TITLE="Homework"

WIDTH=400
HEIGHT=400

# blue=Actor("blue")
# yellow=Actor("yellow")
green=Actor("green")

# blue.pos=200,200
# yellow.pos=200,200
green.pos=200,200

def draw():
    screen.fill("#00BFFF")
    # blue.draw()
    # yellow.draw()
    green.draw()

def update():
    pass

def on_mouse_down(pos):
    if green.collidepoint(pos):
        green.pos=random.randint(50,200),random.randint(50,200)

pgzrun.go()