import pgzrun
import random

TITLE="Collect the Satelites"

HEIGHT=500
WIDTH=600

sats=[]
lines=[]


number_of_satelites=10
for i in range(0,number_of_satelites):
    satelites=Actor("satelites")
    satelites.x=random.randint(50,WIDTH-100)
    satelites.y=random.randint(50,HEIGHT-100)
    sats.append(satelites)


    
def draw():
    screen.blit("spacebg",(0,0))
    number=1

    for i in sats:
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        i.draw()
        number+=1
    
    for i in lines:
        screen.draw.line(i[0],i[1],"white")


def update():
    pass




pgzrun.go()