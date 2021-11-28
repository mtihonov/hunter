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

    bolls = Group()
    hf.new_bolls(h_settings, screen, bolls)
    area = Area(h_settings, screen)
    play_button = Button(h_settings, screen, "Play")
    quit_button


    while True:
        hf.check_events(h_settings, screen, area)
        hf.update_screen(h_settings, screen, bolls, area)
        area.update()
        hf.bolls_update(h_settings, screen, bolls, area)

run_game()