# -*- encoding: utf-8 -*-
"""
@File       : 9.Contours等高线图.py
@Time       : 2020/9/30 19:19
@Author     : Hans
@Software   : PyCharm
"""


import matplotlib.pyplot as plt
import numpy as np


def f(q, t):
    # the height function
    return (1 - q / 2 + q ** 5 + t ** 3) * np.exp(-q ** 2 - t ** 2)  # np.exp(x)为e的x次方


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

# use plt.contourf to filling contours
# X, Y and value for (X, Y) point
plt.contourf(X, Y, f(X, Y), 10, alpha=0.75, cmap=plt.cm.hot)  # cmap颜色，plt.cm.hot就是让人感觉热的颜色，填充十种颜色
# contorf()填充轮廓
# use plt.contour to add contour lines
C = plt.contour(X, Y, f(X, Y), 10, colors='black', linewidths=.5)  # 10条等高线
# contourf()绘制轮廓线
# adding label
plt.clabel(C, inline=True, fontsize=10)  # inline=True表示线不穿过数字，更美观

plt.xticks(())
plt.yticks(())

plt.show()
