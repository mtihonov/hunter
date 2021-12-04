import pygame
import sys
from boll import Boll
import json


def update_screen(h_settings, screen, sb, play_button, quit_button, bolls, area, stats):
    """Обновляет изображения на экране и отображает новый экран."""
    screen.fill(h_settings.bg_color)

    # Выводит на экран мяч
    for boll in bolls.sprites():
        boll.blitme()

    # Выводит на экран площадку.
    area.blitme()

    checking_the_exit_from_the_screen(h_settings, screen, bolls, stats, sb)

    sb.prep_score()
    sb.show_score()

    # Вывод кнопок на экран
    if not stats.game_active:
        if stats.boll_left <= 0:
            load_image_game_over(h_settings, screen)
            sb.show_score_game_over()

        play_button.draw_button()
        quit_button.draw_button()

    pygame.display.flip()

def check_collisions(h_settings, screen, stats, sb, bolls, area):
    """Проверка столкновения мяча и площадки."""
    if pygame.sprite.spritecollideany(area, bolls):
        checking_the_current_and_record_account(stats, sb)
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

def check_events(h_settings, screen, stats, sb, area, play_button, quit_button):
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
            check_play_button(h_settings, screen, stats, sb, play_button, quit_button, mouse_x, mouse_y)

def check_play_button(h_settings, screen, stats, sb, play_button, quit_button, mouse_x, mouse_y):
    """Запускает или закрывает игру при нажатии мышкой на кнопки"""
    play_button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if play_button_clicked and not stats.game_active:
        # Сбро игровых настроек.
        # ai_settings.initialize_dynamic_settings()
        # Указатель мыши скрывается.
        pygame.mouse.set_visible(False)

        stats.reset_stats()
        sb.prep_bolls()
        stats.game_active = True

    quit_button_clicked = quit_button.rect.collidepoint(mouse_x, mouse_y)
    if quit_button_clicked:
        sys.exit()

def bolls_update(h_settings, screen, stats, sb, bolls, area):
    """Обновление позиции мяча."""
    bolls.update()
    check_collisions(h_settings, screen, stats, sb, bolls, area)

def checking_the_exit_from_the_screen(h_settings, screen, bolls, stats, sb):
    """Удаляет мяч и выводит картинку о конце игры."""
    for boll in bolls.copy():
        if boll.rect.y >= h_settings.screen_height:
            stats.boll_left -= 1
            sb.prep_bolls()

            if stats.boll_left > 0:
                del_bolls(bolls)
                new_bolls(h_settings, screen, bolls)
            else:
                stats.game_active = False
                pygame.mouse.set_visible(True)
                del_bolls(bolls)
                new_bolls(h_settings, screen, bolls)

def checking_the_current_and_record_account(stats, sb):
    stats.score += stats.get_score
    sb.prep_score()

    if stats.score >= stats.high_score:
        stats.high_score = stats.score
        filename = 'high_score.json'
        with open(filename, 'w') as f_obj:
            json.dump(stats.score, f_obj)
        sb.prep_high_score()