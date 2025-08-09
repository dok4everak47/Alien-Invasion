import sys

import pygame

from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):

    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    pygame.display.flip()


<<<<<<< HEAD
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键按下事件，设置飞船移动标志"""
=======
def check_keydown_events(event, ship):
    """
    Purpose:
    """

>>>>>>> parent of d4f537d (增加上下移动)
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
<<<<<<< HEAD
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
=======


# end def
>>>>>>> parent of d4f537d (增加上下移动)


def check_keyup_events(event, ship):
    """
    Purpose:
    """

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


# end def
