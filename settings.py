class Settings():

    def __init__(self):
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (249, 180, 222)

        self.unicorn_speed_factor = 3
        self.unicorn_limit = 3

        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        self.rainbow_speed_factor = 2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        self.rainbow_points = 50

    def initialize_dynamic_settings(self):
        self.unicorn_speed_factor = 3
        self.bullet_speed_factor = 10
        self.rainbow_speed_factor = 2
        self.fleet_direction = 1

        self.rainbow_points = 50

    def increase_speed(self):
        self.unicorn_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.rainbow_speed_factor *= self.speedup_scale

        self.rainbow_points = int(self.rainbow_points * self.score_scale)
        print(self.rainbow_points)
