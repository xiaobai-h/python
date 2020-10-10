# -*- encoding: utf-8 -*-
"""
@File       : 13.图中图.py
@Time       : 2020/10/3 14:47
@Author     : Hans
@Software   : PyCharm
"""


import matplotlib.pyplot as plt

fig = plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(y, x, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title inside 1')

left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(x, y, 'b')

plt.axes([0.6, 0.2, 0.25, 0.25])
plt.plot(y[::-1], x, 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')

plt.show()
