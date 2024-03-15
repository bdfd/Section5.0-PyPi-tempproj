'''
Date         : 2023-11-08 15:22:18
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2024-03-15 10:31:17
LastEditors  : <BDFD>
Description  : 
FilePath     : \unittest\supervised_classification\regression\Tele_Customer_Churn_0602.py
Copyright (c) 2023 by BDFD, All Rights Reserved. 
'''
# '''
# Date         : 2023-11-08 12:57:48
# Author       : BDFD,bdfd2005@gmail.com
# Github       : https://github.com/bdfd
# LastEditTime : 2023-11-08 13:11:30
# LastEditors  : BDFD
# Description  :
# FilePath     : \unittest\supervised_classification\regression\Tele_Customer_Churn_0602.py
# Copyright (c) 2023 by BDFD, All Rights Reserved.
# '''

import pandas as pd
import numpy as np
import execdata as exe
import tempproj as temp

para_list = []
SeniorCiitizen = 'No'
para_list.append(SeniorCiitizen)
Partner = 'No'
para_list.append(Partner)
Dependents = 'No'
para_list.append(Dependents)
tenure = 7
para_list.append(tenure)
OnlineSecurity = 'No'
para_list.append(OnlineSecurity)
TechSupport = 'No'
para_list.append(TechSupport)
Contract = 'Monthly'
para_list.append(Contract)
PaperlessBilling = 'Yes'
para_list.append(PaperlessBilling)
PaymentMethod = 'Mailed Cheque'
para_list.append(PaymentMethod)
MonthlyCharges = 79.75
para_list.append(MonthlyCharges)
print(para_list)
result = temp.supervised_classification.Tele_Customer_Churn_0602(para_list)
# print(transformed_sample_df)
# result = model.predict(transformed_sample_df)
print(result)
# print(type(result))
