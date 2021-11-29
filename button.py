import pygame.font

class Button():

    def __init__(self, h_settings, screen, msg, x, y):
        """Инициализирует атрибуты кнопки."""
        self.ai_settings = h_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.screen_rect.x = x
        self.screen_rect.y = y

        # Назачение размеров и свойств кнопок.
        self.width = 200
        self.height = 50
        self.button_color = (0, 0, 0)
        self.text_color = (0, 255, 0)
        self.font = pygame.font.SysFont('Boncegro FF 4F', 36)

        # Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = self.screen_rect.x
        self.rect.y = self.screen_rect.y


        # Сообщение кнопки создается только дин раз.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Отображение пустой кнопки и вывод сообщения."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)