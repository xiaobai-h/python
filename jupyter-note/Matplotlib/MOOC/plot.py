# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 20:38:47 2020

@autor:  Hans
@blog :  https://hancode.top
@email:  501560987@qq.com
"""


# plt.plot(x, y, format_string, **kwargs)
import matplotlib.pyplot as plt
import numpy as np

a = np.arange(10)
plt.plot(a, a*1.5, 'go-', a, a*2.5, 'rx', a, a*3.5, '*', a, a*4.5, 'b-.')
plt.show()

# format_string: 控制曲线的格式字符串，可选有颜色字符、风格字符和标记字符组成
'''
color: 控制颜色，color='green'
linestyle: 线条风格，linestyle='dashed'
marker: 标记风格，marker='o'
'''
