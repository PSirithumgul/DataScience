import pandas as pd

# Sample dataset
data = {'Shirt_Size': ['Extra_Small', 'Extra_Small', 'Small', 'Small', 'Extra_Large', 'Medium', 'Large',  'Medium', 'Large']}
df = pd.DataFrame(data)

# Custom mapping for shirt sizes
size_mapping = {
    'Extra_Small': 0,
    'Small': 1,
    'Medium': 2,
    'Large': 3,
    'Extra_Large': 4
}

# Encoding shirt sizes based on the custom mapping
df['Shirt_Size_Encoded'] = df['Shirt_Size'].map(size_mapping)
print("Label Encoded DataFrame:\n", df)
