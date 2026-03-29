import pgzrun
import random
from time import time


TITLE="Collect the Satelites"

HEIGHT=500
WIDTH=600

sats=[]
lines=[]
next_satelite=0

start_time=0
end_time=0
total_time=0

number_of_satelites=10
def create_satelites():
    global start_time
    for i in range(0,number_of_satelites):
        satelites=Actor("satelites")
        satelites.x=random.randint(50,WIDTH-100)
        satelites.y=random.randint(50,HEIGHT-100)
        sats.append(satelites)
    start_time=time()


    
def draw():
    global total_time
    screen.blit("spacebg",(0,0))
    number=1

    for i in sats:
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        i.draw()
        number+=1
    
    for i in lines:
        screen.draw.line(i[0],i[1],"white")

    if next_satelite<number_of_satelites:
        total_time=time()-start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)

    else:
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)


def update():
    pass

def on_mouse_down(pos):
    global next_satelite,lines
    if next_satelite<number_of_satelites:
        if sats[next_satelite].collidepoint(pos):
            if next_satelite:
                lines.append((sats[next_satelite-1].pos,sats[next_satelite].pos))
            next_satelite=next_satelite+1

        else:
            lines=[]
            next_satelite=0

create_satelites()


pgzrun.go()