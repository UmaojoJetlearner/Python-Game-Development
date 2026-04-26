import pgzrun
import random
from time import time


TITLE="Collect the Stars"

HEIGHT=500
WIDTH=600

stars=[]
lines=[]
next_star=0

start_time=0
end_time=0
total_time=0

number_of_star=10
def create_star():
    global start_time
    for i in range(0,number_of_star):
        Star=Actor("star")
        Star.x=random.randint(50,WIDTH-100)
        Star.y=random.randint(50,HEIGHT-100)
        stars.append(Star)
    start_time=time()


    
def draw():
    global total_time
    screen.blit("spacebg",(0,0))
    number=1

    for i in stars:
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        i.draw()
        number+=1
    
    for i in lines:
        screen.draw.line(i[0],i[1],"white")

    if next_star<number_of_star:
        total_time=time()-start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)

    else:
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)


def update():
    pass

def on_mouse_down(pos):
    global next_star,lines
    if next_star<number_of_star:
        if stars[next_star].collidepoint(pos):
            if next_star:
                lines.append((stars[next_star-1].pos,stars[next_star].pos))
            next_star=next_star+1

        else:
            lines=[]
            next_star=0

create_star()


pgzrun.go()