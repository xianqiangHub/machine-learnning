#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2019/10/8 17:25
# @Author: jiaxianqiang

import numpy as np

# np_array = np.arange(10)
#二维数组，可以转化为矩阵，但不等同于矩阵。
#我们通常会说矩阵的维度，这里的维度也不是指的空间，而是指矩阵的行数。
#

np_array = [[[1,2,3],[4,5,6]],[[7,8,9],[2,3,4]]]

nd_array = np.array(np_array)
print(nd_array)
print(nd_array.ndim)
print(nd_array.shape)





