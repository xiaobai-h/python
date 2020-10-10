# -*- encoding: utf-8 -*-
"""
@File       : figure图像.py
@Time       : 2020/9/29 10:54
@Author     : Hans
@Software   : PyCharm
"""

import matplotlib.pyplot as plt
import numpy as np

# plt.figure()
x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

# plt.plot(x, y1)
plt.figure(num=3, figsize=(8, 5))  # 图像编号或者名称， 指定图片宽高
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.5, linestyle='--')
plt.show()
