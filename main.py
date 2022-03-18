from assets import *
from characters.Enemy import Enemy
from characters.Player import Player
import emoji

def main():
    run = True
    level = 0
    lives = 5
    lost = False
    wave_length = 5

    clock = pygame.time.Clock()
    player = Player(300, 650)
    current_enemies = []

    def redraw_window():
        draw_asset(BACKGROUND, 0, 0)
        draw_text(f"Lives: {emoji.emojize('❤') * lives}", 10, 10, COLOR_RED)
        draw_text(f"Level: {level}", 10, 10, COLOR_WHITE, True)
        player.draw()
        draw_text(f"enemies={len(current_enemies)}", 375, 50)
        if lost:
            draw_text_centered("You lost!!!")

        for current_enemy in current_enemies:
            current_enemy.draw()

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True

        if len(current_enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                new_enemy = Enemy()
                current_enemies.append(new_enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = get_keys()

        player.move_x(keys[pygame.K_d] - keys[pygame.K_a])
        player.move_y(keys[pygame.K_s] - keys[pygame.K_w])

        for enemy in current_enemies[:]:
            enemy.move(ENEMY_VELOCITY)
            if enemy.out_of_y_bounds():
                lives -= 1
                current_enemies.remove(enemy)


main()
