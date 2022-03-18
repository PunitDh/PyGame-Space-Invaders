import os

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


# Enemy ships
def asset_loader(asset):
    return pygame.image.load(os.path.join("assets", asset + ".png"))
# end


RED_SPACE_SHIP = asset_loader("pixel_ship_red_small")
GREEN_SPACE_SHIP = asset_loader("pixel_ship_green_small")
BLUE_SPACE_SHIP = asset_loader("pixel_ship_blue_small")

# Player ship
YELLOW_SPACE_SHIP = asset_loader("pixel_ship_yellow")

# Lasers
RED_LASER = asset_loader("pixel_laser_red")
GREEN_LASER = asset_loader("pixel_laser_green")
BLUE_LASER = asset_loader("pixel_laser_blue")
YELLOW_LASER = asset_loader("pixel_laser_yellow")

# Background
BACKGROUND = pygame.transform.scale(asset_loader("background-black"), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Enemy map
ENEMY_COLOR_MAP = {
    "red": (RED_SPACE_SHIP, RED_LASER),
    "green": (GREEN_SPACE_SHIP, GREEN_LASER),
    "blue": (BLUE_SPACE_SHIP, BLUE_LASER),
}