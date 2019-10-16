#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2019/10/14 10:58
# @Author: jiaxianqiang

import numpy as np
import pandas as pd

# cand_nm – 接受捐赠的候选人姓名
# contbr_nm – 捐赠人姓名
# contbr_st – 捐赠人所在州
# contbr_employer – 捐赠人所在公司
# contbr_occupation – 捐赠人职业
# contb_receipt_amt – 捐赠数额（美元）
# contb_receipt_dt – 收到捐款的日期

data_1 = pd.read_csv('D:\Code\github\machine-learnning\data_lab\data_01.csv', encoding='gbk')
data_2 = pd.read_csv('D:\Code\github\machine-learnning\data_lab\data_02.csv', encoding='gbk')

data = pd.concat([data_1, data_2])
# print(data[data['contb_receipt_amt'] < 0]['contb_receipt_amt'])
# print(sum(pd.isnull(data['contbr_employer'])))   此列数据有多少空值
# print(data.info())
data['contbr_employer'].fillna('NOT PROVIDED', inplace=True)  # True 修改原对象
data['contbr_occupation'].fillna('NOT PROVIDED', inplace=True)

# 看候选人个数
# print(data['cand_nm'].unique())  #去重返回的是ndarray  个数用的len()
parties = {'Bachmann, Michelle': 'Republican',
           'Cain, Herman': 'Republican',
           'Gingrich, Newt': 'Republican',
           'Huntsman, Jon': 'Republican',
           'Johnson, Gary Earl': 'Republican',
           'McCotter, Thaddeus G': 'Republican',
           'Obama, Barack': 'Democrat',
           'Paul, Ron': 'Republican',
           'Pawlenty, Timothy': 'Republican',
           'Perry, Rick': 'Republican',
           "Roemer, Charles E. 'Buddy' III": 'Republican',
           'Romney, Mitt': 'Republican',
           'Santorum, Rick': 'Republican'}

# 通过字典 候选人名字映射出党派 增加一列
data['party'] = data['cand_nm'].map(parties)
# data['party'].value_counts()   #党派及其出现次数
# 按照职业汇总对赞助总金额进行排序
data.groupby('contbr_occupation')['contb_receipt_amt'].sum().sort_values(ascending=False)[:20]

# 由于不同职业名字对应相同职业类型，进行映射，字典有的映射，没有的还是原来的
# 获取一列，map映射，使用lambda
# 建立一个职业对应字典，把相同职业的不同表达映射为对应的职业，比如把C.E.O.映射为CEO
occupation_map = {
    'INFORMATION REQUESTED PER BEST EFFORTS': 'NOT PROVIDED',
    'INFORMATION REQUESTED': 'NOT PROVIDED',
    'SELF': 'SELF-EMPLOYED',
    'SELF EMPLOYED': 'SELF-EMPLOYED',
    'C.E.O.': 'CEO',
    'LAWYER': 'ATTORNEY',
}
f = lambda x: occupation_map.get(x, x)
data.contbr_occupation.map(f)

emp_mapping = {
    'INFORMATION REQUESTED PER BEST EFFORTS': 'NOT PROVIDED',
    'INFORMATION REQUESTED': 'NOT PROVIDED',
    'SELF': 'SELF-EMPLOYED',
    'SELF EMPLOYED': 'SELF-EMPLOYED',
}

# If no mapping provided, return x
f = lambda x: emp_mapping.get(x, x)
data.contbr_employer = data.contbr_employer.map(f)

# 通过一列的booble值删选，条件获取数据
data[data['contb_receipt_amt'] > 0]

bins = np.array([0, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000])
labels = pd.cut(data['contb_receipt_amt'], bins)
print(labels)
