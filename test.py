import pandas as pd
import numpy as np
import tempproj as temp

model = temp.Car_Prediction()
# print(model)
prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'], data=np.array(
    ['Maruti Suzuki Swift', 'Maruti', 2019, 100, 'Petrol']).reshape(1, 5)))
result = str(np.round(prediction[0], 2))
print(result)
print(type(result))
