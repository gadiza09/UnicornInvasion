import sys

import pygame

from pygame.sprite import Group

from settings import Settings

from game_stats import GameStats

from scoreboard import Scoreboard

from unicorn import Unicorn

from rainbow import Rainbow

import game_functions as gf

from button import Button


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Unicorn Invasion")

    play_button = Button(ai_settings, screen, "PLAY")

    stats = GameStats(ai_settings)

    sb = Scoreboard(ai_settings, screen, stats)

    bg_color = (249, 180, 222)

    unicorn = Unicorn(ai_settings, screen)
    bullets = Group()
    rainbows = Group()

    gf.create_fleet(ai_settings, screen, unicorn, rainbows)

    # rainbow = Rainbow(ai_settings, screen)

    pygame.mixer.music.load("song/UnicornsSong.mp3")
    pygame.mixer.music.play(-1, 0.0)

    while True:

        gf.check_events(ai_settings, screen, stats, sb, play_button, unicorn, rainbows, bullets)

        if stats.game_active:
            unicorn.update()
            gf.update_bullets(ai_settings, screen, stats, sb, unicorn, rainbows, bullets)
            gf.update_rainbows(ai_settings, stats, screen, sb, unicorn, rainbows, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, unicorn, rainbows, bullets, play_button)



run_game()

