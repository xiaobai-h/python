# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 18:08:56 2020

@author:  Hans
@blog :  https://hancode.top
@email:  501560987@qq.com
"""


import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'SimHei'
plt.plot([3, 1, 4, 5, 2])
plt.ylabel("纵轴(值)")
plt.savefig('test', dpi=600)
plt.show()
'''
font.family: 用于显示字体的名字
font.style: 字体风格，正常 'normal' 或者斜体 'italic'
font.size: 字体大小，整数字号或者 'large'、'x-small'

rcParams['font.family'] :
    'SimHei': 中文黑体
    'Kaiti': 中文楷体
    'LiSu': 中文隶书
    'FangSong': 中文仿宋
    'YouYuan': 中文幼圆
    'STSong': 华文宋体   
'''
