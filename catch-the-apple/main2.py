from numpy import place
import pgzrun
import random

WIDTH = 800
HEIGHT = 600

apple = Actor('apple')

score = 0

def draw():
    screen.clear()
    screen.draw.text('Score: {}'.format(score),pos=(10,10),color='white')
    apple.draw()

def place_an_apple():
    apple.x = random.randint(10,790)
    apple.y = random.randint(10,590)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print('Catched!!')  
    else:
        print('Missed')
    place_an_apple()


place_an_apple()



pgzrun.go()