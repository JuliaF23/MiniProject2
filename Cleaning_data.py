import pandas as pd  

df = pd.read_csv("netflix_data.csv")

# Remove extra spaces in column names
df.columns = df.columns.str.strip()

# Remove extra spaces in all text columns
str_columns = df.select_dtypes(include='object').columns
df[str_columns] = df[str_columns].apply(lambda x: x.str.strip())

# Convert the 'date_added' column to date format
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Print column data types
print("Column data types:")
print(df.dtypes)

# Show how many missing values each column has
print("\nMissing values per column:")
print(df.isnull().sum())

# Saving a new CSV file with cleaned data
df.to_csv("netflix_cleaned.csv", index=False)
print("\nCleaned data saved to 'netflix_cleaned.csv'")
