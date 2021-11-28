import pygame
import sys
from boll import Boll


def update_screen(h_settings, screen, bolls, area):
    """Обновляет изображения на экране и отображает новый экран."""
    screen.fill(h_settings.bg_color)
    for boll in bolls.sprites():
        boll.blitme()
    area.blitme()
    checking_the_exit_from_the_screen(h_settings, screen, bolls)
    if check_collisions(h_settings, screen, bolls, area):
        del_bolls(bolls)
        new_bolls(h_settings, screen, bolls)
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

def check_events(h_settings, screen, area):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, h_settings, area)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, h_settings, area)

def bolls_update(h_settings, screen, bolls, area):
    """Обновление позиции мяча."""
    bolls.update()

def checking_the_exit_from_the_screen(h_settings, screen, bolls):
    """Удаляет мяч и выводит."""
    for boll in bolls.copy():
        if boll.rect.y >= h_settings.screen_height:

            h_settings.boll_limit -= 1
            if h_settings.boll_limit < 0:
                load_image_game_over(h_settings, screen)
            else:
                del_bolls(bolls)
                new_bolls(h_settings, screen, bolls)
