import pygame
from settings_hunter import Settings
import hunter_function as hf
from pygame.sprite import Group
from area import Area
from button import Button
from game_stats import GameStats

def run_game():
    """Инициализирует игру и создает объект экрана."""
    pygame.init()
    h_settings = Settings()
    screen = pygame.display.set_mode((h_settings.screen_width, h_settings.screen_height))
    pygame.display.set_caption("Hunter")

    # Создание мяча
    bolls = Group()
    hf.new_bolls(h_settings, screen, bolls)

    # Создание площадки
    area = Area(h_settings, screen)

    # Создание кнопок для начала и конца игры
    play_button = Button(h_settings, screen, "Play", 350, 500)
    quit_button = Button(h_settings, screen, "Quit", 800, 500)

    # Создание экземпляра для хранения игровой статистики
    stats = GameStats(h_settings)

    while True:
        hf.check_events(h_settings, screen, stats, area, play_button, quit_button)
        hf.update_screen(h_settings, screen, play_button, quit_button, bolls, area, stats)
        if stats.game_active:
            area.update()
            hf.bolls_update(screen, bolls)

run_game()