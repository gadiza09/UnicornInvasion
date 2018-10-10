class GameStats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

        self.game_active = False

    def reset_stats(self):
        self.unicorn_left = self.ai_settings.unicorn_limit