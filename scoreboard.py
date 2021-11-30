import pygame.font

from pygame.sprite import Group

from boll import Boll

class Scoreboard():
    """Класс для вывода игровой информации."""
    def __init__(self, h_settings, screen, stats):
        """ Инициализирует атрибуты подсчета очков."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.h_settings = h_settings
        self.stats = stats

        # Настройки шрифта для вывода счетва.
        self.text_color = (209, 126, 43)
        self.font = pygame.font.SysFont('Boncegro FF 4F', 25)

        # Подготовка исходного изображения.
        self.prep_score()
        self.prep_high_score()
        self.prep_bolls()

    def prep_score(self):
        """Преобразует текущий счет в графическое изображение."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render('Поймано мячей - ' + score_str, True, self.text_color,
                                            self.h_settings.bg_color)

        # Вывод счета в правой верхней части экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Выводит счет на экран."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

        # Вывод кораблей.
        self.bolls.draw(self.screen)

    def prep_high_score(self):
        """Преобразует рекордный счет в графическое изображение."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render('Рекорд: ' + high_score_str, True, self.text_color,
                                                 self.h_settings.bg_color)

        # Рекордно выравнивается по центру верхней стороны.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_bolls(self):
        """ Сообщает количетво оставшихся краблей."""
        self.bolls = Group()
        for boll_number in range(self.stats.boll_left):
            boll = Boll(self.h_settings, self.screen)
            boll.rect.x = 10 + boll_number * boll.rect.width
            boll.rect.y = 10
            self.bolls.add(boll)