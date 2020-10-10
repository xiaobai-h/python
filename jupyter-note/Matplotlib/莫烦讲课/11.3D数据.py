# -*- encoding: utf-8 -*-
"""
@File       : 3D数据.py
@Time       : 2020/10/1 8:15
@Author     : Hans
@Software   : PyCharm
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)  # 一句话解释numpy.meshgrid()——生成网格点坐标矩阵。关键词：网格点，坐标矩阵
R = np.sqrt(X ** 2 + Y ** 2)
# height value
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
ax.contourf(X, Y, Z, zdir='x', offset=-4, cmap='rainbow')
ax.set_zlim(-2, 2)
plt.show()
