# -*- encoding: utf-8 -*-
"""
@File       : 设置坐标轴.py
@Time       : 2020/9/29 18:30
@Author     : Hans
@Software   : PyCharm
"""


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am x')
plt.ylabel('I am y')

new_ticks = np.linspace(-1, 2, 5)
# print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3, ],
           ['really bad', 'bad', 'normal', 'good', 'really good'])

# gca = 'get current axis'
# data:移动轴的位置到交叉轴的指定坐标  outward:不太懂  axes:0.0 - 1.0之间的值，整个轴上的比例  center:('axes',0.5) zero:('data',0.0)
ax = plt.gca()
ax.spines['right'].set_color('none')  # 右边框去掉
ax.spines['top'].set_color('none')  # 左边框去掉
ax.xaxis.set_ticks_position('bottom')  # 将底边框设置为x轴
ax.yaxis.set_ticks_position('left')  # 将做边框设置为y轴
ax.spines['bottom'].set_position(('data', -1))  # 改变坐标轴
ax.spines['left'].set_position(('data', 0))

plt.show()
