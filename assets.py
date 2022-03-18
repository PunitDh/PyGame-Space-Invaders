import os

import pygame

from constants import WINDOW, SCREEN_WIDTH, get_font, SCREEN_HEIGHT, COLOR

pygame.display.set_caption("Space Shooter")


def asset_loader(asset):
    return pygame.image.load(os.path.join("assets", asset + ".png"))
# end


def draw_asset(asset, x, y, right_aligned=False):
    return WINDOW.blit(asset, (SCREEN_WIDTH - asset.get_width() - x if right_aligned else x, y))
# end


def draw_text(text, x, y, color=COLOR["white"], right_aligned=False, font_size=30):
    f = get_font(font_size).render(text, True, color)
    return draw_asset(f, x, y, right_aligned)
# end


def draw_text_centered(text, color=COLOR["white"], font_size=30):
    f = get_font(font_size).render(text, True, color)
    return draw_asset(f, (SCREEN_WIDTH-f.get_width())/2, (SCREEN_WIDTH-f.get_height())/2)
# end


def draw_rect(x, y, height, width, color, offset=10):
    return pygame.draw.rect(WINDOW, color, (x, y + height + offset, width, 10))
# end


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None
# end


# Enemy ships
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

ENEMY_COLOR_MAP = {
    "red": (RED_SPACE_SHIP, RED_LASER),
    "green": (GREEN_SPACE_SHIP, GREEN_LASER),
    "blue": (BLUE_SPACE_SHIP, BLUE_LASER),
}
