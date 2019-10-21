#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2019/10/17 11:31
# @Author: jiaxianqiang

import numpy as np
import pandas as pd

# PassengerId	乘客编号
# Survived	存活情况（存活：1 ; 死亡：0）
# Pclass	客舱等级
# Name	乘客姓名
# Sex	性别
# Age	年龄
# SibSp	同乘的兄弟姐妹/配偶数
# Parch	同乘的父母/小孩数
# Ticket	船票编号
# Fare	船票价格
# Cabin	客舱号
# Embarked	登船港口

ti_train_data = pd.read_csv('D:\Code\github\machine-learnning\data_lab\\titanic_train.csv', encoding='gbk')
ti_test_data = pd.read_csv('D:\Code\github\machine-learnning\data_lab\\titanic_test.csv', encoding='gbk')

# print(ti_train_data.info())
# 特征提取，PassengerId和判断幸存无关不做特征列，Cabin空值较多，多是否幸存影响不到，填充空值影响更大，暂不做特征列
# 年龄也有空值，空值不多，对是否幸存结果影响很大，