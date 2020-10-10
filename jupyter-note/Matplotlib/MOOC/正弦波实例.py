# -*- encoding: utf-8 -*-
"""
@File       : 正弦波实例.py
@Time       : 2020/9/28 19:06
@Author     : Hans
@Software   : PyCharm
"""

import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0.0, 5.0, 0.02)
plt.plot(a, np.cos(2*np.pi*a), 'r--')

plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=15, color='green')
plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=15)
plt.title(r'正弦波实例 $y=cos(2\pi x)$', fontproperties='SimHei', fontsize=25)
# plt.text(2, 1, r'$\mu=100$', fontsize=15)  # 显示在(2,1)上，显示内容为第三项，
plt.annotate(r'$\mu=100$', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.1, width=2))
# 注释：注释内容，指向位置，内容位置，内容选项(箭头颜色，箭头和文本之间空白，箭头宽度)

plt.axis([-1, 6, -2, 2])  # 横纵轴坐标范围
plt.grid(True)  # 加入网格绘制曲线
plt.show()
