#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2019/10/9 18:24
# @Author: jiaxianqiang

import numpy as np
import pandas as pd

arange = np.array([3, 4, 5, 6, 7, 8]).reshape(2, 3)

stu_dic = {'Age': [14, 13, 13, 14, 14, 12, 12, 15, 13, 12, 11, 14, 12, 15, 16, 12, 15, 11, 15],
           'Height': [69, 56.5, 65.3, 62.8, 63.5, 57.3, 59.8, 62.5, 62.5, 59, 51.3, 64.3, 56.3, 66.5, 72, 64.8, 67,
                      57.5, 66.5],
           'Name': ['Alfred', 'Alice', 'Barbara', 'Carol', 'Henry', 'James', 'Jane', 'Janet', 'Jeffrey', 'John',
                    'Joyce', 'Judy', 'Louise', 'Marry', 'Philip', 'Robert', 'Ronald', 'Thomas', 'Willam'],
           'Sex': ['M', 'F', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'F', 'F', 'M', 'M', 'M', 'M', 'M'],
           'Weight': [112.5, 84, 98, 102.5, 102.5, 83, 84.5, 112.5, 84, 99.5, 50.5, 90, 77, 112, 150, 128, 133, 85,
                      112]}
student = pd.DataFrame(stu_dic)
student['Kaa'] = [11, 1, 1, 1, 1, 1, 7, 8, 9, 10, 11, 1, 2, 12, 1, 1, 1, 3, 3]

# print(student.groupby('Sex').mean())
print(student['Age'] > 12)

occupation_map = {
    'INFORMATION REQUESTED PER BEST EFFORTS': 'NOT PROVIDED',
    'INFORMATION REQUESTED': 'NOT PROVIDED',
    'SELF': 'SELF-EMPLOYED',
    'SELF EMPLOYED': 'SELF-EMPLOYED',
    'C.E.O.': 'CEO',
    'LAWYER': 'ATTORNEY',
}

# print(occupation_map.get('aaa','bb'))
