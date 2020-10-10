# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 20:12:45 2020

@author: hsx13
"""

import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


a = np.arange(0.0, 5.0, 0.02)

plt.subplot(211)
plt.plot(a, 2*a)

plt.subplot(2, 1, 2)
plt.plot(a, np.cos(2*np.pi*a), 'r--')
plt.show()
