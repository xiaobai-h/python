# -*- encoding: utf-8 -*-
"""
@File       : 7.Scatter散点图.py
@Time       : 2020/9/30 18:44
@Author     : Hans
@Software   : PyCharm
"""


import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)

plt.scatter(X, Y, c=T, s=75, alpha=0.5)
# plt.scatter(np.arange(5), np.arange(5))

plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))
plt.xticks(())
plt.yticks(())

plt.show()
