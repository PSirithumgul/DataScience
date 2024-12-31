import pandas as pd
import numpy as np

# Define the dataset
data = {
    "ID": [1, 2, 3, 4, 5, 5, 6, 7, 8],
    "Name": ["John Doe", np.nan, "Jane Doe", "Jim Smith", "Ana Bell", "Ana Bell", "Chris O'Neil", "Mike Brown", "Susan Clark"],
    "Age": [29, 34, 27, 29.5, 24, 24, 25, np.nan, 28],
    "Height": [170, np.nan, 168, 171, 169, 169, 167, 172, np.nan],
    "Weight": [np.nan, 70.5, 55, 60.2, np.nan, np.nan, 70, 68, 55],
    "City": ["New York", "Bangkok", np.nan, "Chicago", "Los Angeles", "Los Angeles", "Boston", "Miami", "Paris"],
    "Date_of_Birth": ["01-02-1995", "1990-07-25", "27th August 1997", "12/01/1994", "24-August-2000", "24-August-2000", np.nan, "01-01-1998", "1996/02/01"],
    "Income": [50000, np.nan, 40000, 55000.00, 45000, 45000, 48000, 52000, 49000],
    "Employment_Status": ["Employed", "Unemployed", "Employed", "Employed", "Self-Employed", "Self-Employed", "Unemployed", np.nan, "Employed"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Detect missing values (NaN and blanks)
missing_summary = df.isnull().sum()
print("Missing values per column:\n", missing_summary)

# Show rows with missing values
rows_with_missing = df[df.isnull().any(axis=1)]
print("\nRows with missing values:\n", rows_with_missing)
