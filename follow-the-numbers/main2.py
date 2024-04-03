import random
import pgzrun

WIDTH = 600
HEIGHT = 400

dots = []
lines = []

number = 1
next_number = 0


def create_dots():
    global dots
    dots = []
    for i in range(0,10):
        dot = Actor('dot')
        dot.pos = (random.randint(0,WIDTH - 20),random.randint(0,HEIGHT -20))
        dots.append(dot)
create_dots()

def draw():
    global number, dots
    number = 1
    screen.clear()
    for dot in dots:
        screen.draw.text(str(number),(dot.pos[0],dot.pos[1]+10))
        dot.draw()
        number +=1
    for line in lines:
        screen.draw.line(line[0],line[1],(100,0,0))

def on_mouse_down(pos):
    global dots, lines, next_number
    if dots[next_number].collidepoint(pos):
        if next_number:
            lines.append((dots[next_number-1].pos,dots[next_number].pos))
        next_number += 1
    else:
        lines = []
        next_number = 0
        create_dots()

pgzrun.go()