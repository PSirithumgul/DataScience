import pandas as pd
import numpy as np

# Create the dataset
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8],
    "Age": [25, 30, np.nan, 35, 28, 40, 22, np.nan],  # Numerical data
    "Shirt_Size": ["M", "L", "S", np.nan, "XL", "M", "XS", np.nan],  # Ordinal data
    "Gender": ["Male", "Female", "Female", "Male", np.nan, "Male", "Female", "Female"]  # Nominal data
}

# Load the data into a DataFrame
df = pd.DataFrame(data)

# Define the order for ordinal data
shirt_size_order = {"XS": 1, "S": 2, "M": 3, "L": 4, "XL": 5}

# Map Shirt_Size to numerical values for median calculation
df['Shirt_Size_Encoded'] = df['Shirt_Size'].map(shirt_size_order)

# Impute missing values
# Impute Age (numerical) with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Impute Shirt_Size (ordinal) with median
median_shirt_size = df['Shirt_Size_Encoded'].median()
df['Shirt_Size_Encoded'] = df['Shirt_Size_Encoded'].fillna(median_shirt_size)

# Reverse map Shirt_Size_Encoded to original categories
reverse_shirt_size_order = {v: k for k, v in shirt_size_order.items()}
df['Shirt_Size'] = df['Shirt_Size_Encoded'].map(reverse_shirt_size_order)

# Impute Gender (nominal) with mode
df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])

# Drop the encoded column
df = df.drop(columns=['Shirt_Size_Encoded'])

# Display the cleaned DataFrame
print("DataFrame after imputing missing values:\n", df)
