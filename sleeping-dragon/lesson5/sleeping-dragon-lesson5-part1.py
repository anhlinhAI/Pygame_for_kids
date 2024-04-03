import math
import pgzrun


WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)


FONT_COLOR = (0, 0, 0)


EGG_TARGET = 20
HERO_START = (200, 300)
ATTACK_DISTANCE = 200 
DRAGON_WAKE_TIME = 2
EGG_HIDE_TIME = 2
MOVE_DISTANCE = 5

lives = 3
eggs_collected = 0
game_over = False
game_complete = False
reset_required = False

