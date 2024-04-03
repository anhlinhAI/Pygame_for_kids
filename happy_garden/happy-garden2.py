import pgzrun
import time
import random

WIDTH = 800
HEIGHT = 600

start_time = time.time()

flower_list = []
wilted_list = []

#C1: cow = Actor('cow',(100,500))
#C2
cow = Actor('cow')
cow.pos = (100,500)

game_over = False

def draw():
    if not game_over:
        screen.clear()

        screen.blit('garden',(0,0))
        cow.draw()

        time_elapsed = int(time.time() - start_time)
        screen.draw.text(f'Garden is happy for {time_elapsed} seconds', topleft = (10,10), color = 'white')

        for flower in flower_list:
            flower.draw()

def update():
    pass

def new_flower():
    global flower_list, wilted_list
    x_random = random.randint(50, WIDTH - 50)
    y_random = random.randint(50, HEIGHT - 50)
    flower = Actor('flower')
    flower.pos = (x_random, y_random)
    flower_list.append(flower)
    wilted_list.append('happy')

new_flower()

pgzrun.go()