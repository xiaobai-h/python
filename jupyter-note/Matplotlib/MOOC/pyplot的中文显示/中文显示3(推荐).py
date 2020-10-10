# -*- encoding: utf-8 -*-
"""
@File       : 中文显示3(推荐).py
@Time       : 2020/9/28 18:44
@Author     : Hans
@Software   : PyCharm
"""
# 再有中文输出的地方，增加一个属性：fontproperties
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0.0, 5.0, 0.02)

plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=20)
plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=20)
plt.plot(a, np.cos(2*np.pi*a), 'r--')
plt.show()
