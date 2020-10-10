# -*- encoding: utf-8 -*-
"""
@File       : 12.Subplot显示.py
@Time       : 2020/10/1 8:45
@Author     : Hans
@Software   : PyCharm
"""


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec


def delete_ticks(ax):  # 删除边框数据，更美观但不直接显示数据
    ax.set_xticks(())
    ax.set_yticks(())


'''方法一：直接在subplot中选定位置'''
# plt.figure()
#
# plt.subplot(2, 1, 1)
# plt.plot([0, 1], [0, 1])
#
# plt.subplot(2, 3, 4)
# plt.plot([0, 1], [0, 2])

# plt.show()

'''方法二'''
# method 1:subplot2grid
#########################
# plt.figure()
# x = np.linspace(0, 2*np.pi, 50)
# y1 = np.cos(x)
# ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
# ax1.plot(x, y1)
# delete_ticks(ax1)
# ax1.set_title('Line')  # 第一张图
#
# ax2 = plt.subplot2grid((3, 3), (1, 2), colspan=1, rowspan=1)
# x = np.random.random(100)
# y = np.random.random(100)
# ax2.scatter(x, y, c=np.arctan2(y, x), alpha=0.5)
# delete_ticks(ax2)
# ax2.set_title('Scatter')
#
# ax3 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=1)
# x = np.arange(100)
# y = np.sin(x)
# ax3.bar(x, y)
# delete_ticks(ax3)
# ax3.set_title('Bar')
#
# ax4 = plt.subplot2grid((3, 3), (2, 0), colspan=1, rowspan=1)
# pie_sizes = [10.0, 20.0, 30.0, 40.0]
# pie_labels = ['gao', 'yuan', 'chai', 'Hans']
# ax4.pie(pie_sizes, labels=pie_labels)
# ax4.set_title('Pie')
""" 饼状图说明
x       :(每一块)的比例，如果sum(x) > 1会使用sum(x)归一化；
labels  :(每一块)饼图外侧显示的说明文字；
explode :(每一块)离开中心距离；
startangle :起始绘制角度,默认图是从x轴正方向逆时针画起,如设定=90则从y轴正方向画起；
shadow  :在饼图下面画一个阴影。默认值：False，即不画阴影；
labeldistance :label标记的绘制位置,相对于半径的比例，默认值为1.1, 如<1则绘制在饼图内侧；
autopct :控制饼图内百分比设置,可以使用format字符串或者format function
        '%1.1f'指小数点前后位数(没有用空格补齐)；
pctdistance :类似于labeldistance,指定autopct的位置刻度,默认值为0.6；
radius  :控制饼图半径，默认值为1；counterclock ：指定指针方向；布尔值，可选参数，默认为：True，即逆时针。将值改为False即可改为顺时针。
wedgeprops ：字典类型，可选参数，默认值：None。参数字典传递给wedge对象用来画一个饼图。例如：wedgeprops={'linewidth':3}设置wedge线宽为3。
textprops ：设置标签（labels）和比例文字的格式；字典类型，可选参数，默认值为：None。传递给text对象的字典参数。
center ：浮点类型的列表，可选参数，默认值：(0,0)。图标中心位置。
frame ：布尔类型，可选参数，默认值：False。如果是true，绘制带有表的轴框架。
rotatelabels ：布尔类型，可选参数，默认为：False。如果为True，旋转每个label到指定的角度。
"""

'''方法三  最好用'''
# plt.figure(num=3)
# x = np.linspace(0, 10, 100)
# gs = gridspec.GridSpec(3, 3)
# ax1 = plt.subplot(gs[0, :])
# ax1.plot(x, np.sin(x))
# ax2 = plt.subplot(gs[1, :2])
# ax3 = plt.subplot(gs[1:, 2])
# ax4 = plt.subplot(gs[-1, 0])
# ax5 = plt.subplot(gs[-1, -2])

'''方法四'''
f, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1, 2], [1, 2])
ax11.grid()  # 显示网格
plt.tight_layout()
plt.show()
