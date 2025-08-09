import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from bullet import Bullet


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    bg_color = (230, 230, 230)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 存储子弹的编组
    bullets = Group()

    # 创建一个外星人
    # alien = Alien(ai_settings, screen)

    # 创建外星人Group
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

        # 让外星人移动
        gf.update_aliens(ai_settings, aliens)

        # 每次循环都重绘屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
