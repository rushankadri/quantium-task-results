import pandas as pd

# This tells Python WHERE the files are
file_paths = [
    'data/daily_sales_data_0.csv', 
    'data/daily_sales_data_1.csv', 
    'data/daily_sales_data_2.csv'
]

# Combine the files
df = pd.concat((pd.read_csv(f) for f in file_paths), ignore_index=True)

# Filter for Pink Morsels
df = df[df['product'] == 'pink morsel']

# Fix the price and calculate sales
df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)
df['sales'] = df['price'] * df['quantity']

# Keep only necessary columns
df = df[['sales', 'date', 'region']]

# Save the result
df.to_csv('formatted_output.csv', index=False)
print("Success! formatted_output.csv created.")