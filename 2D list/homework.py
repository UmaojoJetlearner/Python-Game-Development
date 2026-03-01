import pgzrun
import random 

TITLE="Hit BLUE!"

WIDTH=500
HEIGHT=500

score=0

message=""

blue=Actor("blue")
# alien.x=50
# alien.y=50

blue.pos=250,250

def draw():
    screen.fill("#ffa200de")
    blue.draw()
    screen.draw.text(message,center=(300,10),fontsize=30) 
    screen.draw.text("Score:"+str(score),center=(300,30),fontsize=30)
def update():
    pass


def on_mouse_down(pos):
    global message,score
    if blue.collidepoint(pos):
        blue.pos=random.randint(50,400),random.randint(50,400)
        message="Nice hit!"
        score=score+1
        
    else:
       message="Try again.."
       score=score-1

pgzrun.go()
