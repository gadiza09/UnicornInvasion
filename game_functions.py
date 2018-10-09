import sys

import pygame

from bullets import Bullet

def check_keydown_events(event, ai_settings, screen, unicorn, bullets):
    if event.key == pygame.K_RIGHT:
        unicorn.moving_right = True
    elif event.key == pygame.K_LEFT:
        unicorn.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, unicorn, bullets)

def fire_bullet(ai_settings, screen, unicorn, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, unicorn)
        bullets.add(new_bullet)


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


def update_screen(ai_settings, screen, unicorn, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    unicorn.blitme()

def update_bullets(bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


    pygame.display.flip()
