from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Sample dataset
data = {'Shirt_Size': ['Extra_Small', 'Extra_Small', 'Small', 'Small', 'Extra_Large', 'Medium', 'Large',  'Medium', 'Large']}
df = pd.DataFrame(data)

# Label Encoding
label_encoder = LabelEncoder()
df['Shirt_Size_Encoded'] = label_encoder.fit_transform(df['Shirt_Size'])
print("Label Encoded DataFrame:\n", df)
