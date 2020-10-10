# -*- encoding: utf-8 -*-
"""
@File       : subplot2grid().py
@Time       : 2020/9/28 20:02
@Author     : Hans
@Software   : PyCharm
"""

import matplotlib.pyplot as plt

plt.subplot2grid((3, 3), (0, 0), colspan=3)
plt.subplot2grid((3, 3), (1, 0), colspan=2)
plt.subplot2grid((3, 3), (1, 2), rowspan=2)
plt.subplot2grid((3, 3), (2, 0))
plt.subplot2grid((3, 3), (2, 1))
plt.show()
