import pygame.mask

from utils import collide
from constants import WINDOW, SCREEN_HEIGHT


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    # end

    def draw(self):
        WINDOW.blit(self.img, (self.x, self.y))
    # end

    def move(self, vel):
        self.y += vel
    # end

    def below_screen(self):
        return self.y >= SCREEN_HEIGHT
    # end

    def above_screen(self):
        return self.y <= 0
    # end

    def collision(self, obj):
        return collide(self, obj)
    # end
# end
