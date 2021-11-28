class Settings():
    """Класс для хранения настроек игры Hunter."""
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1360
        self.screen_height = 710
        self.bg_color = (255, 255, 255)

        # Скорость перемещения мяча.
        self.speed_boll = 0.2

        # Количество одновременнонаходящихся мячей в игре.
        self.quantity_boll = 1

        # Количество попыток.
        self.boll_limit = 3

        # атрибуты площадки
        self.speed_area = 1.0
        self.area_width = 150
        self.area_height = 10
        self.area_color = 60, 60, 60


