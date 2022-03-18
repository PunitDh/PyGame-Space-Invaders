import pygame

pygame.font.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 750, 750
FPS = 60

COLOR = {
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (0, 255, 255)
}

PLAYER_VELOCITY = 5
ENEMY_VELOCITY = 1
PLAYER_LASER_VELOCITY = 8
ENEMY_LASER_VELOCITY = 4


WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

fonts = pygame.font.get_fonts()
emojis = [font for font in fonts if "emoji" in font]


def get_font(size=30):
    return pygame.font.SysFont(emojis[0], size)
# end


def get_keys():
    return pygame.key.get_pressed()
# end


def seconds(val):
    return FPS * val
# end