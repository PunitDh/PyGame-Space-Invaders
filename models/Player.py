import random
from assets import YELLOW_SPACE_SHIP, YELLOW_LASER
from constants import PLAYER_VELOCITY, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_LASER_VELOCITY
from models.Ship import Ship


class Player(Ship):
    def __init__(self, health=100):
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT - 150
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.laser_damage = random.randrange(60, 80)
        super().__init__(x, y, health, self.ship_img, self.laser_img, self.laser_damage)
    # end

    def move_lasers(self, objs):
        self.cool_down()
        for laser in self.lasers:
            laser.move(-PLAYER_LASER_VELOCITY)
            if laser.above_screen():
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        obj.health -= self.laser_damage
                        self.lasers.remove(laser)
                    # end
                # end
            # end
        # end
    # end

    def move_x(self, qty):
        vel = qty * PLAYER_VELOCITY
        if self.within_x_bounds(vel):
            self.x += vel
        # end
    # end

    def move_y(self, qty):
        vel = qty * PLAYER_VELOCITY
        if self.within_y_bounds(vel):
            self.y += vel
    # end
# end
