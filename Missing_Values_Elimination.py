import pandas as pd
import numpy as np

# Create a dataset with 3% missing values
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Name": ["John Doe", np.nan, "Jane Doe", "Jim Smith", "Ana Bell", "Chris O'Neil", "Mike Brown", "Susan Clark", "Oliver Twist", "Emily Rose"],
    "Age": [29, 34, 27, 29.5, 24, 25, np.nan, 28, 35, 30],
    "Height": [170, np.nan, 168, 171, 169, 167, 172, np.nan, 175, 165],
    "Weight": [np.nan, 70.5, 55, 60.2, np.nan, 70, 68, 55, 75, 60],
    "City": ["New York", "Bangkok", "Paris", "Chicago", "Los Angeles", "Boston", np.nan, "Miami", "London", "San Francisco"],
    "Income": [50000, np.nan, 40000, 55000, 45000, 48000, 52000, 49000, 9999999999, 60000],
    "Employment_Status": ["Employed", "Unemployed", "Employed", "Employed", "Self-Employed", "Unemployed", "Employed", "Employed", "Self-Employed", np.nan]
}

# Calculate total values and 3% of it for missing data validation
total_values = sum(len(col) for col in data.values())
missing_values = sum(pd.isnull(val).sum() for val in data.values())
missing_percentage = (missing_values / total_values) * 100
print(f"Total values: {total_values}, Missing values: {missing_values}, Missing Percentage: {missing_percentage:.2f}%")

# Load the data into a DataFrame
df = pd.DataFrame(data)

# Display the initial DataFrame
print("Original DataFrame:\n", df)

# Drop rows with missing values (NaN or blanks)
df_cleaned = df.dropna()

# Display the cleaned DataFrame
print("\nDataFrame after eliminating rows with missing values:\n", df_cleaned)
