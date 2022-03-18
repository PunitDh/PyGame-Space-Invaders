import os
from constants import *

pygame.display.set_caption("Space Shooter")


def asset_loader(asset):
    return pygame.image.load(os.path.join("assets", asset + ".png"))
# end


def draw_asset(asset, x, y, right_aligned=False):
    return WINDOW.blit(asset, (SCREEN_WIDTH - asset.get_width() - x if right_aligned else x, y))
# end


def draw_text(text, x, y, color=COLOR_WHITE, right_aligned=False):
    f = FONT.render(text, True, color)
    return draw_asset(f, x, y, right_aligned)
# end


def draw_text_centered(text, color=COLOR_WHITE):
    f = FONT.render(text, True, color)
    return draw_asset(f, (SCREEN_WIDTH-f.get_width())/2, (SCREEN_WIDTH-f.get_height())/2)
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

COLOR_MAP = {
    "red": (RED_SPACE_SHIP, RED_LASER),
    "green": (GREEN_SPACE_SHIP, GREEN_LASER),
    "blue": (BLUE_SPACE_SHIP, BLUE_LASER),
}