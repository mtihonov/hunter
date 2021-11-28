import pygame
from pygame.sprite import Sprite
from random import randint
class Boll(Sprite):
    """Класс, представляющий мяч."""

    def __init__(self, h_settings, screen):
        """Класс, инициализирующий натройки мяча и определяющий его положение."""
        super(Boll, self).__init__()
        self.h_settings = h_settings
        self.screen = screen
        self.image = pygame.image.load('images/round_1.bmp.bmp')
        self.rect = self.image.get_rect()

        # Создание мяча
        self.rect.x = randint(10, 1350)
        self.rect.y = randint(10, 300)

        # Позиция мяча хранится в вещественном формате.
        self.y = float(self.rect.y)

        # Количество попыток.
        #self.boll_limit = 0

    def blitme(self):
        """Вывод пули на экран."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += self.h_settings.speed_boll
        # Обновление позиции прямоугольника.
        self.rect.y = self.y

    #def update_boll_limit(self):
        #"""Инициализирует изменене количества попыток."""
        #self.boll_left = self.boll_limit