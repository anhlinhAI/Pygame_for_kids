import pgzrun
import time
import random

WIDTH = 800
HEIGHT = 600

start_time = time.time()

cow = Actor('cow')
cow.pos = 100,500

flower_list = []
wilted_list = []
game_over = False

def draw():
    if not game_over:
        time_elapsed = int(time.time() - start_time)
        screen.blit('garden',(0,0))
        cow.draw()
        for flower in flower_list:
            flower.draw()
        screen.draw.text("Garden is happy for: "+str(time_elapsed), topleft = (10,10),color="white")
    else:
        screen.draw.text("Game over", center = (WIDTH/2, HEIGHT/2),color="white", fontsize = 40)

def update():
    pass

def new_flower():
    global flower_list, wilted_list
    flower = Actor('flower')
    flower.pos = random.randint(50, WIDTH - 50), random.randint(50,HEIGHT - 50)
    flower_list.append(flower)
    wilted_list.append('happy')

new_flower()

pgzrun.go()