import pandas as pd
import numpy as np
import execdata as exe
import tempproj as temp

model, sample_le = temp.supervised_classification.Tele_Customer_Churn_0602()
df_sample_columns = ['SeniorCitizen',
                     'Partner',
                     'Dependents',
                     'tenure',
                     'OnlineSecurity',
                     'TechSupport',
                     'Contract',
                     'PaperlessBilling',
                     'PaymentMethod']
test_sample = (pd.DataFrame(columns=df_sample_columns, data=np.array(
    [0, 'Yes', 'Yes', 10, 'No', 'No', 'One year', 'No', 'Mailed Cheque']).reshape(1, 9)))
# print(test_sample)
transformed_sample_df = exe.data_preprocessing.transform_label_encode(
    test_sample, test_sample.columns, sample_le)
MontlyCharges = 49.55
transformed_sample_df['MonthlyCharges'] = MontlyCharges
# print(transformed_sample_df)
result = model.predict(transformed_sample_df)
print(result[0])
