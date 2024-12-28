import pandas as pd

# Sample dataset
data = {'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']}
df = pd.DataFrame(data)

# One-Hot Encoding and converting boolean to integer
one_hot_encoded = pd.get_dummies(df, columns=['Color']).astype(int)
print("One-Hot Encoded DataFrame:\n", one_hot_encoded)
