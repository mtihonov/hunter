import json

class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, h_settings):
        """Инициализирует статистику."""
        self.h_settings = h_settings
        self.boll_limit = 3
        self.reset_stats()
        self.game_active = False

        # Рекорд не жолжен сбрасываться.
        self.high_score = []
        self.filename = 'high_score.json'
        try:
            with open(self.filename) as f_obj:
                self.high_score = json.load(f_obj)
        except FileNotFoundError:
            self.high_score = 0
            pass
    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.boll_left = self.boll_limit
        self.score = 0