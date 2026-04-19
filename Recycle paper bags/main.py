import pgzrun
import random

WIDTH=800
HEIGHT=600

ITEMS=["plasticbag","battery","bottle","chips"]
items=[]
animations=[]
START_SPEED=10
current_level=1
game_over=False
game_complete=False
final_level=6

def draw():
    screen.clear()
    screen.blit("mainbg",(0,0))
    for i in items:
        i.draw()
        
def update():
    pass

def get_option_to_create(number_of_extra_items):
    items_to_create= ["paper"]
    for i in range(0,number_of_extra_items):
        random_option=random.choice(ITEMS)
        items_to_create.append(random_option)

def create_items(items_to_create):
    new_items=[]
    for option in items_to_create:
        item=Actor(option+"img")
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    number_of_gaps=len(items_to_layout)+1
    gap_size= WIDTH/number_of_gaps
    random.shuffle(items_to_layout)
    for index, items in enumerate(items_to_layout):
        new_x_pos=(index+1)*gap_size
        item.x=new_x_pos

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration=START_SPEED-current_level
        item.anchor=("center","bottom")
        animation=animate(item,duration=duration, on_finished=handle_game_over, y= HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over=True

def on_mouse_down(pos):
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handle_game_complete()

            else:
                handle_game_over()

def handle_game_complete():
    global current_level,items,animations,game_complete
    stop_animations(animations)
    if current_level==final_level:
        game_complete=True

    else:
        current_level+=1
        items=[]
        animations=[]

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()


pgzrun.go()