import pgzrun
from random import randint
apple = Actor("apple")
WIDTH = 800
HEIGHT = 600

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)
    
def on_mouse_down(pos):
    global score, string
    if apple.collidepoint(pos):
        print('Good Shot!!')
        place_apple()
    else:
        print('You missed!!') 
        quit()
place_apple()

pgzrun.go()