import pgzrun
import time
import random

WIDTH = 800
HEIGHT = 600

start_time = time.time()


def draw():
    screen.blit('garden',(0,0))
    time_elapsed = int(time.time() - start_time)
        

pgzrun.go()