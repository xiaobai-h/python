# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 19:35:59 2020

@author: hsx13
"""

import matplotlib.pyplot as plt

plt.plot([0, 2, 4, 6, 8], [3, 1, 4, 5, 2])
plt.ylabel("Grade")
plt.axis([-1, 10, 0, 6])  # x轴起始于-1，终止于10；y轴起始于0，终止于6
plt.show()
'''
plt.subplot(nrows, ncols, plot_number)  对应nrows个横区域，ncols个纵区域，绘制于
plot_number, 也可以直接plt.subplot(345)
'''