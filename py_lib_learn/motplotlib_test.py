#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2019/10/17 10:59
# @Author: jiaxianqiang

import matplotlib.pyplot as plt
#数据可视化

# 导入Matploylib库from matplotlib import pyplot as plt
# #在notebook中画图%matplotlib inline
# #画布上画图plt.plot([1,2,3],[4,5,1])
# #在画布上显示plt.show()
x = [5, 2, 7]
y = [2, 16, 4]
# 图片的标题plt.title('Image Title')
# #坐标轴Y轴plt.ylabel('Y axis')
# #坐标轴X轴plt.xlabel('X axis')
# plt.plot(x, y)
# plt.ylabel("aa")
# plt.show()

from matplotlib import style

# 使用自带的样式进行美化
style.use('ggplot')
x = [5, 8, 10]
y = [12, 16, 6]
plt.plot(x, y, 'g', label='line one', linewidth=6)  # label 线代表的意义
# 设置图例位置 各种符号和颜色所代表内容与指标的说明
plt.legend()
#网格
plt.grid(True, color='k')
plt.show()
