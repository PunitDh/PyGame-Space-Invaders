import pygame

pygame.font.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 750, 750
FPS = 60

COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELLOW = (0, 255, 255)

PLAYER_VELOCITY = 5
ENEMY_VELOCITY = 3

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

fonts = pygame.font.get_fonts()
emojis = [font for font in fonts if "emoji" in font]
FONT = pygame.font.SysFont(emojis[0], 30)


def get_keys():
    return pygame.key.get_pressed()
# end
