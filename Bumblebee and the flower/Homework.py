import random
import pgzrun

TITLE="Get the star"

WIDTH=500
HEIGHT=500

score=0

gameover=False

spaceship=Actor("spaceship")
star=Actor("glowingstar")

spaceship.pos=250,250
def moveflower(): 
    star.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)

def draw():
    screen.blit("spaceimage",(0,0))
    spaceship.draw()    
    star.draw()
    screen.draw.text("Score:"+str(score),center=(70,30),fontsize=50)
    if gameover:
        screen.fill("red")
        screen.draw.text(f"Game Over \n your final score is {score}",color="black",center=(250,250),fontsize=50)

def update():
    global score
    if keyboard.left:
        spaceship.x-=2

    if keyboard.right:
        spaceship.x+=2

    if keyboard.up:
        spaceship.y-=2

    if keyboard.down:
        spaceship.y+=2

    if spaceship.colliderect(star):
        moveflower()
        score+=10
def timeup():
    global gameover
    gameover=True

moveflower()
clock.schedule(timeup,20.0)
pgzrun.go()