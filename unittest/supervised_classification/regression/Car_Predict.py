'''
Date         : 2023-11-06 14:08:41
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-11-06 14:43:07
LastEditors  : BDFD
Description  :
FilePath     : \unittest\supervised_classification\regression\Car_Predict.py
Copyright (c) 2023 by BDFD, All Rights Reserved.
'''

import pandas as pd
import numpy as np
import tempproj as temp

model = temp.supervised_classification.Car_Prediction()
# print(model)
prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'], data=np.array(
    ['Maruti Suzuki Swift', 'Maruti', 2019, 100, 'Petrol']).reshape(1, 5)))
result = str(np.round(prediction[0], 2))
print(result)
print(type(result))
