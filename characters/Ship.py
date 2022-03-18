from constants import *


class Ship:
    def __init__(self, x, y, ship_img=None, laser_img=None, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = ship_img
        self.laser_img = laser_img
        self.lasers = []
        self.cool_down_counter = 0
        self.max_health = health
    # end

    def draw(self):
        WINDOW.blit(self.ship_img, (self.x, self.y))
    # end

    def get_width(self):
        return self.ship_img.get_width()
    # end

    def get_height(self):
        return self.ship_img.get_height()
    # end

    def within_x_bounds(self, qty):
        return 0 < self.x + qty < (SCREEN_WIDTH - self.get_width())
    # end

    def within_y_bounds(self, qty):
        return 0 < self.y + qty < (SCREEN_HEIGHT - self.get_height())
    # end
# end
