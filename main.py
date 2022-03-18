import random

import pygame

from assets import draw_asset, BACKGROUND, draw_text, draw_text_centered, collide
from constants import FPS, seconds, get_keys, ENEMY_VELOCITY, COLOR, LASER_VELOCITY
from models.Enemy import Enemy
from models.Player import Player


def main():
    run = True
    level = 0
    lives = 5
    lost = False
    lost_count = 0
    wave_length = 5

    clock = pygame.time.Clock()
    player = Player(300, 650)
    current_enemies = []

    def redraw_window():
        draw_asset(BACKGROUND, 0, 0)
        draw_text(f"Lives: {'❤' * lives}", 10, 10, COLOR["red"])
        draw_text(f"Level: {level}", 10, 10, COLOR["white"], True)
        player.draw()
        draw_text(f"enemies={len(current_enemies)}", 375, 50)
        if lost:
            draw_text_centered("You lost!!!", COLOR["white"], 60)
        # end

        for current_enemy in current_enemies:
            current_enemy.draw()
        # end

        pygame.display.update()
    # end

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1
        # end

        if lost:
            if lost_count > seconds(3):
                run = False
            else:
                continue
            # end
        # end

        if len(current_enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                new_enemy = Enemy()
                current_enemies.append(new_enemy)
            # end
        # end

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # end
        # end

        keys = get_keys()

        player.move_x(keys[pygame.K_d] - keys[pygame.K_a])
        player.move_y(keys[pygame.K_s] - keys[pygame.K_w])

        if keys[pygame.K_SPACE]:
            player.shoot()
        # end

        for enemy in current_enemies[:]:
            enemy.move(ENEMY_VELOCITY)
            enemy.move_lasers(LASER_VELOCITY, player)

            if random.randrange(0, seconds(4)) == 1:
                enemy.shoot()
            # end

            if collide(enemy, player):
                player.health -= enemy.collision_damage
                current_enemies.remove(enemy)
            elif enemy.out_of_y_bounds():
                lives -= 1
                current_enemies.remove(enemy)
            elif enemy.health <= 0:
                current_enemies.remove(enemy)
            # end
        # end

        player.move_lasers(-LASER_VELOCITY, current_enemies)
    # end
# end


main()
