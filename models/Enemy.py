import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_COLOR_MAP
from models.Laser import Laser
from models.Ship import Ship


class Enemy(Ship):
    def __init__(self):
        random_color = random.choice(list(ENEMY_COLOR_MAP.keys()))
        self.ship_img, self.laser_img = ENEMY_COLOR_MAP[random_color]
        x_value = random.randrange(self.get_width(), SCREEN_WIDTH - self.get_width())
        y_value = random.randrange(-1500, -100)
        laser_damage = random.randrange(5, 15)
        health = random.randrange(50, 150)
        self.collision_damage = 10
        super().__init__(x_value, y_value, health, self.ship_img, self.laser_img, laser_damage)
    # end

    def move(self, vel):
        self.y += vel
    # end

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x - self.get_width() / 4, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
        # end
    # end

    def out_of_y_bounds(self):
        return self.y > SCREEN_HEIGHT
    # end
# end
