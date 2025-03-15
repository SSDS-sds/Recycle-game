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

game_over = False
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











pgzrun.go()