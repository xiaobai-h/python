# -*- encoding: utf-8 -*-
"""
@File       : GridSpec类.py
@Time       : 2020/9/28 20:26
@Author     : Hans
@Software   : PyCharm
"""

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt

gs = gridspec.GridSpec(3, 3)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1, 0: 2])
ax3 = plt.subplot(gs[1:, 2])
ax4 = plt.subplot(gs[2, 0])
ax5 = plt.subplot(gs[2, 1])

plt.show()
