import sys

import pygame

from pygame.sprite import Group

from settings import Settings

from game_stats import GameStats

from unicorn import Unicorn

from rainbow import Rainbow

import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Unicorn Invasion")

    stats = GameStats(ai_settings)

    bg_color = (249, 180, 222)

    unicorn = Unicorn(ai_settings, screen)
    bullets = Group()
    rainbows = Group()

    gf.create_fleet(ai_settings, screen, unicorn, rainbows)

    # rainbow = Rainbow(ai_settings, screen)


    while True:

        gf.check_events(ai_settings, screen, unicorn, bullets)

        if stats.game_active:
            unicorn.update()
            gf.update_bullets(ai_settings, screen, unicorn, rainbows, bullets)
            gf.update_rainbows(ai_settings, stats, screen, unicorn, rainbows, bullets)
            #gf.update_rainbow(ai_settings, stats, screen, unicorn, rainbow, bullets)
        gf.update_screen(ai_settings, screen, unicorn, rainbows, bullets)
        # print(rainbows)


run_game()

