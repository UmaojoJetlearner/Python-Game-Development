import pgzrun
import random 

TITLE="Good Shot"

WIDTH=500
HEIGHT=500

score=0

message=""

alien=Actor("alien")
# alien.x=50
# alien.y=50

alien.pos=250,250

def draw():
    screen.fill("#2784cc")
    alien.draw()
    screen.draw.text(message,center=(300,10),fontsize=30) 
    screen.draw.text("Score:"+str(score),center=(300,30),fontsize=30)
def update():
    pass


def on_mouse_down(pos):
    global message,score
    if alien.collidepoint(pos):
        alien.pos=random.randint(50,400),random.randint(50,400)
        message="Good shot"
        score=score+1
        
    else:
       message="You missed"
       score=score-1

pgzrun.go()


