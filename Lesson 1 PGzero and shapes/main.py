import pgzrun

WIDTH=300
HEIGHT=300

width=20
height=30
def draw():
    rect = Rect((0,0),(width,height))
    screen.draw.rect(rect,("blue"))

def update():
    pass

pgzrun.go()