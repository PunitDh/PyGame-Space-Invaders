from assets import *
from characters.Ship import Ship


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
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
