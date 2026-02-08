import pgzrun
import random



WIDTH=300
HEIGHT=300

width=WIDTH
height=HEIGHT-200

r=random.randint(0,255)
g=random.randint(122,255)
b=0
def draw():
    global width,height,b
    for i in range(20):
        rect = Rect((0,0),(width,height))
        rect.center=(150,150)
        screen.draw.rect(rect,(r,g,b))
        width-=10
        height+=10
        
def update():
    pass

pgzrun.go()