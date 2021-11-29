import pygame
from settings_hunter import Settings
import hunter_function as hf
from pygame.sprite import Group
from area import Area
from button import Button

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


    while True:
        hf.check_events(h_settings, screen, area)
        hf.update_screen(h_settings, screen, play_button, quit_button, bolls, area)
        area.update()
        hf.bolls_update(h_settings, screen, bolls, area)


run_game()