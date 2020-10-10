# -*- encoding: utf-8 -*-
"""
@File       : Bar柱状图.py
@Time       : 2020/9/30 18:59
@Author     : Hans
@Software   : PyCharm
"""


import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)  # 均匀分布
Y2 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, Y1, facecolor='red', edgecolor='white')
plt.bar(X, -Y2, facecolor='yellow', edgecolor='white')

for x, y in zip(X, Y1):
    # ha: horizontal alignment
    plt.text(x+0, y+0.05, '%.2f' % y, ha='center', va='bottom')
for x, y in zip(X, Y2):
    plt.text(x + 0, -y - 0.05, '-%.2f' % y, ha='center', va='top')

plt.xlim(-.5, n)
plt.xticks(())  # 让坐标显示空
plt.ylim(-1.25, 1.25)
plt.yticks(())

plt.show()
