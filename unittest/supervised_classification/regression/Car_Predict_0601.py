'''
Date         : 2023-11-06 14:08:41
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-11-06 17:12:05
LastEditors  : BDFD
Description  :
FilePath     : \Car_Predict_0601.py
Copyright (c) 2023 by BDFD, All Rights Reserved.
'''

import pandas as pd
import numpy as np
import tempproj as temp

para_list = []
name = 'Maruti Suzuki Swift'
para_list.append(name)
company = 'Maruti'
para_list.append(company)
year = 2019
para_list.append(year)
kms_driven = 100
para_list.append(kms_driven)
fuel_type = 'Petrol'
para_list.append(fuel_type)
print(para_list)
result = temp.supervised_classification.Car_Prediction_0601(para_list)
print(result)
print(type(result))
