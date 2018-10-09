import sys

import pygame

from settings import Settings

from unicorn import Unicorn

import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Unicorn Invasion")

    unicorn = Unicorn(ai_settings, screen)

    bullets = Group()

    bg_color = (249, 180, 222)

    while True:

        gf.check_events(ai_settings, screen, unicorn, bullets)
        unicorn.update()
        bullets.update()
        gf.update_bullets(bullets)
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings, screen, unicorn, bullets)


run_game()

