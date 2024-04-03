import pgzrun

WIDTH = 800
HEIGHT = 600
CENTERX = 400
CENTERY = 300
say_dance = True
show_countdown = True
moves_complete = False
game_over = False

move_list = []
display_list = []
score = 0
countdown = 4
currentmove = 0
danceleght = 0

dancer = Actor('dancer-start')
dancer.pos = (CENTERX,CENTERY - 10)

up = Actor("up")
up.pos = CENTERX, CENTERY +110

left = Actor("left")
left.pos = CENTERX - 60, CENTERY + 170

right = Actor("right")
right.pos = CENTERX + 60, CENTERY + 170

down = Actor("down")
down.pos = CENTERX , CENTERY + 230

p1 = Actor("a1")
p1.post = CENTERX - 60, CENTERY 


def draw():
    global game_over,say_dance,show_countdown
    global score, countdown
    if not game_over:
        screen.clear()
        screen.blit ('stage',(0,0))
        dancer.draw()
        up.draw()
        down.draw()
        right.draw()
        left.draw()
        p1.draw()
        screen.draw.text('score: ' + str(score), color = 'black', topleft = (10,10))

        
        if say_dance:
            screen.draw.text('dance!!!!', color = 'black', topleft = (CENTERX - 25,CENTERY),fontsize = 29)
        if show_countdown:
            screen.draw.text(str(countdown),color = 'black', topleft = (CENTERX,CENTERY),fontsize = 30)
    else:
        screen.clear()
        screen.blit ('stage',(0,0))
        screen.draw.text('score: ' + str(score), color = 'black', topleft = (10,10))
        screen.draw.text('game over',color = 'black', topleft = (30,30))
    return

def updatedancer(move):
    global game_over
    if not game_over:
        if move == 0:
            p1.image = 'a2'
            dancer.image = 'dancer-up'
            up.image = 'up-lit'
        elif move == 1:
            p1.image = 'a3'
            dancer.image = 'dancer-right'
            right.image = 'right-lit'
        elif move == 2:
            p1.image = 'a4'
            dancer.image = 'dancer-left'
            left.image = 'left-lit'
        else:
            p1.image = 'a5'
            dancer.image = 'dancer-down'
            down.image = 'down-lit'
    return

def reset_game():
    global game_over
    if not game_over:
        p1.image = 'a1'
        dancer.image = 'dancer-start'
        up.image = 'up'
        right.image = 'right'
        left.image = 'left'
        down.image = 'down'
    return

def on_key_up(key):
    global game_over
    if key == keys.UP:
        updatedancer(0)
        clock.schedule(reset_game,1)
        if move_list[current_move] == 0:
            score += 1
            next_move()
    elif key ==keys.RIGHT:
        updatedancer(1)
        clock.schedule(reset_game,1)
        if move_list[current_move] == 1:
            score += 1
            next_move()
    elif key ==keys.LEFT:
        updatedancer(2)
        clock.schedule(reset_game,1)
        if move_list[current_move] == 2:
            score += 1
            next_move()
    elif key ==keys.DOWN:
        updatedancer(3)
        clock.schedule(reset_game,1)
        if move_list[current_move] == 3:
            score += 1
            next_move()
    return

music.play('vanishing-horizon')

def display_moves():
    global display_list
    global say_dance, show_countdown
    if display_list:
        this_move= display_list[0]
        display_list= display_list[1:]
        if this_move ==0:
            updatedancer(0)
            clock.schedule(display_moves,1)
        elif this_move ==1:
            updatedancer(1)
            clock.schedule(display_moves,1)
        elif this_move ==2:
            updatedancer(2)
            clock.schedule(display_moves,1)
        elif this_move ==3:
            updatedancer(3)
            clock.schedule(display_moves,1)
    else:
        say_dance = True
        show_countdown = False
    return

def generate_moves():
    global display_list, move_list
    global dance_length, show_coutdown
    move_list = []
    for i in range(dance_length):
        random_move = random.randint(0,3)
        move_list.append(random_move)
        display_list.append(random_move)
    show_countdown = True
    countdown()
    return

generate_moves()
def next_move():
     global current_move, dance_length,moves_complete
     if current_move < dance_length - 1:
         current_move += 1
    else:
        moves_complete = True
    return

def update():
    global game_over, moves_complete, current_move
    if not game_over:
        if moves_complete:
            generate_moves()
            current_move= 0
            moves_complete = False
    else:
        music.stop()
        

pgzrun.go()
