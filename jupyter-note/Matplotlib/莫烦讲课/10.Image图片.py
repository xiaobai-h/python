# -*- encoding: utf-8 -*-
"""
@File       : 10.Image图片.py
@Time       : 2020/9/30 20:52
@Author     : Hans
@Software   : PyCharm
"""


import matplotlib.pyplot as plt
import numpy as np

# image data
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3, 3)

plt.imshow(a, interpolation='nearest', cmap='bone', origin='upper')
plt.colorbar(shrink=0.9)

plt.xticks(())
plt.yticks(())

plt.show()
