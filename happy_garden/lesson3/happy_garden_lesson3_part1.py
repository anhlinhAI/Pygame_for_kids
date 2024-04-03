from random import randint
import pgzrun
import time

WIDTH = 800
HEIGHT = 600
start_time = time.time()
time_elapsed = 0

game_over = False #kiểm tra game đã kết thúc chưa
finalized = False
garden_happy = True

flower_list = []
wilted_list = []
fangflower_list = []

cow = Actor("cow")
cow.pos = 100,500

def draw():
    global game_over, time_elapsed, finalized
    if not game_over:
        screen.clear() #xóa screen trước để screen sau chồng lên
        screen.blit("garden",(0,0))
        cow.draw()
        for flower in flower_list:
            flower.draw()
        for fangflower in fangflower_list:
            fangflower.draw()
        time_elapsed = int (time.time() - start_time)
        screen.draw.text("Garden happy for: " + str(time_elapsed) +" seconds",
                             topleft=(10,10), color="white")
    else:
        if not garden_happy:
            screen.draw.text("GARDEN UNHAPPY! GAME OVER!", color="black", topleft=(10,50))
            finalized = True
    return

def new_flower():
    global flower_list, wilted_list
    flower_new = Actor("flower")
    flower_new.pos = randint(50, WIDTH - 50), randint(150, HEIGHT - 100)
    flower_list.append(flower_new)
    wilted_list.append("happy")
    return

def add_flowers():
    global game_over
    if not game_over:
        new_flower()
        clock.schedule(add_flowers, 4)
    return

def check_wilt_times():
    global wilted_list, game_over, garden_happy
    if wilted_list:
        for wilted_since in wilted_list:
            if not wilted_since == "happy":
                time_wilted = int(time.time() - wilted_since)
                if time_wilted > 10:
                    garden_happy = False
                    game_over = True
                    break
    return

def wilt_flower():
    global flower_list, wilted_list, game_over
    if not game_over:
        if flower_list:
            rand_flower = randint(0, len(flower_list)-1)
            if flower_list[rand_flower].image == "flower":
                flower_list[rand_flower].image = "flower-wilt"
                wilted_list[rand_flower] = time.time()
        clock.schedule(wilt_flower, 3)
    return


def mutate():
    global flower_list, fangflower_list, fangflower_vx_list, fangflower_vy_list, game_over
    if not game_over and flower_list:
        rand_flower = randint(0, len(flower_list) - 1)
        fangflower_pos_x = flower_list[rand_flower].x
        fangflower_pos_y = flower_list[rand_flower].y
        del flower_list[rand_flower]
        fangflower = Actor("fangflower")
        fangflower.pos = fangflower_pos_x, fangflower_pos_y
        fangflower_list.append(fangflower)
        clock.schedule(mutate, 20)
    return


add_flowers()
wilt_flower()

#để chương trình game cập nhật liên tục, nghĩa là gọi hàm draw liên tục
def update():
    global game_over, flower_list, fangflower_list, time_elapsed
    check_wilt_times()
    if not game_over:
        if time_elapsed > 15 and not fangflower_list:
            mutate()

pgzrun.go()
