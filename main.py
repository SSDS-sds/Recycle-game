import pgzrun
import random

WIDTH = 800
HEIGHT = 600
TITLE = "Recycling game"
CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2
CENTER = (CENTER_X,CENTER_Y)
FINAL_LEVEL = 6
START_SPEED = 10
ITEMS = ["battery","bottle","chips","bag"]

is_game_over = False
game_complete = False
current_level = 1
items = []
animations = []

def draw():
    screen.clear()
    screen.blit("bgimg", (0,0))

def update():
    pass

def get_option(extra_items):
    items_to_create = ["paper"]
    for i in range(extra_items):
        option = random.choice(ITEMS)
        items_to_create.append(option)
    return items_to_create

def create_items(items_to_create):
    new_items = []
    for ites in items_to_create:
        item = Actor(ites + "img")
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    num_gaps = len(items_to_layout) + 1
    gap_size = WIDTH / num_gaps
    random.shuffle(items_to_layout)
    for index, item in enumerate(items_to_layout):
        new_x_pos = (index + 1) * gap_size
        item.x = new_x_pos

def animate_items(items_to_animate):
    global animations 
    for item in items_to_animate:
        duration = START_SPEED - current_level
        item.anchor = ("center", "bottom")
        animation = animate(item, duration = duration, on_finished = game_over, y = HEIGHT)
        animations.append(animation)

def game_over():
    global is_game_over
    is_game_over = True

def on_mouse_down(pos):
    global items,current_level
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handel_game_complete()
            else:
                game_over()





pgzrun.go()