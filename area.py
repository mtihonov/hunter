import pygame
from pygame.sprite import Sprite

class Area(Sprite):
    """Класс, представляющий площадку."""

    def __init__(self, h_settings, screen):
        """Инициализирует атрибуты и методы площадки."""
        super(Area, self).__init__()
        self.screen = screen
        self.h_settings = h_settings

 # Создание площадки в позиции в нижней части экрана.
        self.rect = pygame.Rect(0, 0, h_settings.area_width,
                                h_settings.area_height)
        self.rect.centerx = h_settings.screen_width/2
        self.rect.bottom = h_settings.screen_height - 20
        self.screen_rect = screen.get_rect()

        # Позиция пуди хранится в вещественном формате.
        self.y = float(self.rect.bottom)

        self.color = h_settings.area_color
        self.speed_factor = h_settings.speed_area


        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Вывод площадки на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        """Обновляет позицию корабля с учетом флагов."""
        # Обновляет атрибут center, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.speed_factor


