# -*- encoding: utf-8 -*-
"""
@File       : 1.基本用法.py
@Time       : 2020/9/29 20:10
@Author     : Hans
@Software   : PyCharm
"""


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 2*x + 1

plt.plot(x, y)
plt.show()
