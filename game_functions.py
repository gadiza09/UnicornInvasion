import sys

from time import sleep

import pygame

from bullets import Bullet

from rainbow import Rainbow
import math

def check_keydown_events(event, ai_settings, screen, unicorn, bullets):
    if event.key == pygame.K_RIGHT:
        unicorn.moving_right = True
    elif event.key == pygame.K_LEFT:
        unicorn.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, unicorn, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, unicorn):
    if event.key == pygame.K_RIGHT:
        unicorn.moving_right = False
    elif event.key == pygame.K_LEFT:
        unicorn.moving_left = False


def check_events(ai_settings, screen, unicorn, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, unicorn, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, unicorn)


def fire_bullet(ai_settings, screen, unicorn, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, unicorn)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, stats, unicorn, rainbows, bullets, play_button):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    unicorn.blitme()
    rainbows.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def update_bullets(ai_settings, screen, unicorn, rainbows, bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_rainbows_collisions(ai_settings, screen, unicorn, rainbows, bullets)


def check_bullet_rainbows_collisions(ai_settings, screen, unicorn, rainbows, bullets):
    collisions = pygame.sprite.groupcollide(bullets, rainbows, True, True)
    if len(rainbows) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, unicorn, rainbows)


def check_fleet_edges(ai_settings, rainbows):
    for rainbow in rainbows.sprites():
        if rainbow.check_edges():
            change_fleet_direction(ai_settings, rainbows)
            break


def change_fleet_direction(ai_settings, rainbows):
    for rainbow in rainbows.sprites():
        rainbow.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def unicorn_hit(ai_settings, stats, screen, unicorn, rainbows, bullets):
    if stats.unicorn_left > 0:
        stats.unicorn_left -= 1

    else:
        stats.game_active = False

        rainbows.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, unicorn, rainbows)
        unicorn.center_unicorn()
        sleep(0.5)


def check_rainbows_bottom(ai_settings, stats, screen, unicorn, rainbows, bullets):
    screen_rect = screen.get_rect()
    for rainbow in rainbows.sprites():
        if rainbow.rect.bottom >= screen_rect.bottom:
            unicorn_hit(ai_settings, stats, screen, unicorn, rainbows, bullets)
            break


def update_rainbows(ai_settings, stats, screen, unicorn, rainbows, bullets):
    check_fleet_edges(ai_settings, rainbows)
    rainbows.update()

    if pygame.sprite.spritecollideany(unicorn, rainbows):
        unicorn_hit(ai_settings, stats, screen, unicorn, rainbows, bullets)
        print("Unicorn hit!!!")

    check_rainbows_bottom(ai_settings, stats, screen, unicorn, rainbows, bullets)


def get_number_rainbows_x(ai_settings, rainbow_width):
    available_space_x = ai_settings.screen_width - 2 * rainbow_width
    number_rainbows_x = int(available_space_x / (2 * rainbow_width))
    return number_rainbows_x


def get_number_rows(ai_settings, unicorn_height, rainbow_height):
    available_space_y = (ai_settings.screen_height -
                         (3 * rainbow_height) - unicorn_height)
    number_rows = int(available_space_y / (2 * rainbow_height))
    return number_rows


def create_rainbow(ai_settings, screen, rainbows, rainbow_number, row_number):
    rainbow = Rainbow(ai_settings, screen)
    rainbow_width = rainbow.rect.width
    rainbow.x = rainbow_width + 2 * rainbow_width * rainbow_number
    rainbow.rect.x = rainbow.x
    rainbow.rect.y = rainbow.rect.height + 2 * rainbow.rect.height * row_number
    rainbows.add(rainbow)


def create_fleet(ai_settings, screen, unicorn, rainbows):
    rainbow = Rainbow(ai_settings, screen)
    number_rainbows_x = get_number_rainbows_x(ai_settings, rainbow.rect.width)
    number_rows = get_number_rows(ai_settings, unicorn.rect.height, rainbow.rect.height)

    for row_number in range(number_rows):
        for rainbow_number in range(number_rainbows_x):
            create_rainbow(ai_settings, screen, rainbows, rainbow_number, row_number)

