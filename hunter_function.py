import pygame
import sys
from boll import Boll


def update_screen(h_settings, screen, sb, play_button, quit_button, bolls, area, stats):
    """Обновляет изображения на экране и отображает новый экран."""
    screen.fill(h_settings.bg_color)

    # Выводит на экран мяч
    for boll in bolls.sprites():
        boll.blitme()

    # Выводит на экран площадку.
    area.blitme()

    checking_the_exit_from_the_screen(h_settings, screen, bolls, stats)

    check_collisions(h_settings, screen, bolls, area)

    # Вывод кнопок на экран
    if not stats.game_active:
        if stats.boll_left <= 0:
            load_image_game_over(h_settings, screen)
        play_button.draw_button()
        quit_button.draw_button()

    sb.show_score()

    pygame.display.flip()

def check_collisions(h_settings, screen, bolls, area):
    """Проверка столкновения мяча и площадки."""
    if pygame.sprite.spritecollideany(area, bolls):
        del_bolls(bolls)
        new_bolls(h_settings, screen, bolls)

def load_image_game_over(h_settings, screen):
    """Загрузка изображегния для вывода на случай проигрыша."""
    image = pygame.image.load('images/Game_over.bmp.bmp')
    rect = image.get_rect()
    rect.centerx = h_settings.screen_width / 2
    rect.centery = h_settings.screen_height / 2
    screen.blit(image, rect)

def new_bolls(h_settings, screen, bolls):
    """Создает новый экземпляр мяча."""
    for boll in range(h_settings.quantity_boll):
        boll = Boll(h_settings, screen)
        bolls.add(boll)
    if len(bolls) < h_settings.quantity_boll:
        boll = Boll(h_settings, screen)
        bolls.add(boll)

def del_bolls(bolls):
    """Удаляет мяч после соприкосновения площадки и мяча."""
    bolls.empty()

def check_keydown_events(event, h_settings, area):
    """Реагирует на нажатие клавиш."""
    if event.key == pygame.K_a:
        area.moving_left = True
    elif event.key == pygame.K_d:
        area.moving_right = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, h_settings, area):
    """Реагирует на отпускание клавиш."""
    if event.key == pygame.K_a:
        area.moving_left = False
    elif event.key == pygame.K_d:
        area.moving_right = False

def check_events(h_settings, screen, stats, area, play_button, quit_button):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, h_settings, area)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, h_settings, area)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(h_settings, screen, stats, play_button, quit_button, mouse_x, mouse_y)

def check_play_button(h_settings, screen, stats, play_button, quit_button, mouse_x, mouse_y):
    """Запускает или закрывает игру при нажатии мышкой на кнопки"""
    play_button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if play_button_clicked and not stats.game_active:
        # Сбро игровых настроек.
        # ai_settings.initialize_dynamic_settings()

        # Указатель мыши скрывается.
        pygame.mouse.set_visible(False)

        stats.reset_stats()
        stats.game_active = True
        load_image_game_over(h_settings, screen)

    quit_button_clicked = quit_button.rect.collidepoint(mouse_x, mouse_y)
    if quit_button_clicked:
        sys.exit()

def bolls_update(screen, bolls):
    """Обновление позиции мяча."""
    bolls.update()

def checking_the_exit_from_the_screen(h_settings, screen, bolls, stats):
    """Удаляет мяч и выводит картинку о конце игры."""
    for boll in bolls.copy():
        if boll.rect.y >= h_settings.screen_height:
            stats.boll_left -= 1

            if stats.boll_left > 0:
                del_bolls(bolls)
                new_bolls(h_settings, screen, bolls)
            else:
                stats.game_active = False
                pygame.mouse.set_visible(True)
                del_bolls(bolls)
                new_bolls(h_settings, screen, bolls)
