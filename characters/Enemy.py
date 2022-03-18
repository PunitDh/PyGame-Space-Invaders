import random
import pygame.mask
from assets import *
from characters.Ship import Ship


class Enemy(Ship):
    def __init__(self, health=100):
        random_color = random.choice(list(COLOR_MAP.keys()))
        self.ship_img, self.laser_img = COLOR_MAP[random_color]
        self.mask = pygame.mask.from_surface(self.ship_img)
        x_value = random.randrange(self.get_width(), SCREEN_WIDTH - self.get_width())
        y_value = random.randrange(-1500, -100)
        super().__init__(x_value, y_value, self.ship_img, self.laser_img)
    # end

    def move(self, vel):
        self.y += vel
    # end

    def out_of_y_bounds(self):
        return self.y > SCREEN_HEIGHT
    # end
# end
