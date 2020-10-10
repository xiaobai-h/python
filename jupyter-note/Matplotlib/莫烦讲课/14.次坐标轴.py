# -*- encoding: utf-8 -*-
"""
@File       : 14.次坐标轴.py
@Time       : 2020/10/3 15:06
@Author     : Hans
@Software   : PyCharm
"""


import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = 0.05 * x**2
y2 = -1 * y1

# plt.figure()
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()  # twinx：共享x轴， twiny：共享y轴
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b-')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1', color='g')
ax2.set_ylabel('Y2', color='b')

plt.show()
