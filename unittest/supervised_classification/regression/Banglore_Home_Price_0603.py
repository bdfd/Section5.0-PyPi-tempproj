'''
Date         : 2024-03-15 12:58:12
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2024-03-15 15:52:54
LastEditors  : <BDFD>
Description  : 
FilePath     : \0603.py
Copyright (c) 2024 by BDFD, All Rights Reserved. 
'''
import pandas as pd
import numpy as np
import tempproj as temp

para_list = []
bedroom = 2
para_list.append(bedroom)
square_feet = 1000
para_list.append(square_feet)
bathroom = 2
para_list.append(bathroom)
location = '1st Phase JP Nagar'
para_list.append(location)
print(para_list)
print(para_list[0])
result = temp.supervised_classification.Banglore_Home_Price_Prediction_0603(
    para_list)
print('result is', result)
