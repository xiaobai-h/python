# -*- encoding: utf-8 -*-
"""
@File       : 中文显示2.py
@Time       : 2020/9/28 18:33
@Author     : Hans
@Software   : PyCharm
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'STSong'
matplotlib.rcParams['font.size'] = 20

a = np.arange(0.0, 5.0, 0.02)

plt.xlabel('横轴：时间')
plt.ylabel('纵轴：振幅')
plt.plot(a, np.cos(2*np.pi*a), 'r--')
plt.show()
