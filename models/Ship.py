import pygame.draw

from assets import draw_rect
from constants import WINDOW, SCREEN_WIDTH, SCREEN_HEIGHT, seconds, COLOR, ENEMY_LASER_VELOCITY
from models.Laser import Laser


class Ship:
    COOL_DOWN = seconds(0.5)

    def __init__(self, x, y, health=100, ship_img=None, laser_img=None, laser_damage=10):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = ship_img
        self.laser_img = laser_img
        self.lasers = []
        self.cool_down_counter = 0
        self.max_health = health
        self.laser_damage = laser_damage
        self.mask = pygame.mask.from_surface(self.ship_img)
    # end

    def draw(self):
        WINDOW.blit(self.ship_img, (self.x, self.y))
        self.draw_health_bar()
        for laser in self.lasers:
            laser.draw()
        # end
    # end

    def move_lasers(self, obj):
        self.cool_down()
        for laser in self.lasers:
            laser.move(ENEMY_LASER_VELOCITY)
            if laser.below_screen():
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= self.laser_damage
                self.lasers.remove(laser)
            # end
        # end
    # end

    def cool_down(self):
        if self.cool_down_counter >= self.COOL_DOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1
        # end
    # end

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
        # end
    # end

    def draw_health_bar(self):
        draw_rect(self.x, self.y, self.get_height(), self.get_width(), COLOR["red"])
        draw_rect(self.x, self.y, self.get_height(), self.get_width() * self.health / self.max_health, COLOR["green"])
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
