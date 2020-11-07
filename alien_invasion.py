# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 20:36
# @Author  : ChenMing
# @Email   : 932392374@qq.com
# @USER    : chen
# @File    : alien_invasion.py
# @Software: PyCharm

import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():

    #初始化一个屏幕
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    #开始游戏的主循环
    while True:

        #监视鼠标键盘事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        # 删除已消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        gf.update_screen(ai_settings, screen, ship, bullets)


def main():
    run_game()
    return


if __name__ == "__main__":
    main()