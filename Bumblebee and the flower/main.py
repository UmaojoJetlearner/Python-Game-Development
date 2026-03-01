import random
import pgzrun

TITLE="Get the Flower"

WIDTH=500
HEIGHT=500

score=0

gameover=False

bee=Actor("beeimage")
flower=Actor("flowerimage")

bee.pos=250,250
def moveflower(): 
    flower.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)

def draw():
    screen.blit("grassimage",(0,0))
    bee.draw()    
    flower.draw()
    screen.draw.text("Score:"+str(score),center=(70,30),fontsize=50)
    if gameover:
        screen.fill("red")
        screen.draw.text(f"Game Over \n your final score is {score}",color="black",center=(250,250),fontsize=50)

def update():
    global score
    if keyboard.left:
        bee.x-=2

    if keyboard.right:
        bee.x+=2

    if keyboard.up:
        bee.y-=2

    if keyboard.down:
        bee.y+=2

    if bee.colliderect(flower):
        moveflower()
        score+=10
def timeup():
    global gameover
    gameover=True

moveflower()
clock.schedule(timeup,20.0)
pgzrun.go()