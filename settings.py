# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 20:44
# @Author  : ChenMing
# @Email   : 932392374@qq.com
# @USER    : chen
# @File    : settings.py
# @Software: PyCharm

class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕参数设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #子弹参数设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60

        # 飞船移速设置
        self.ship_speed_factor = 0.5