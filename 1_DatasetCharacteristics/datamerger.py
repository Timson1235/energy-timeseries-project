import pandas as pd

# Load CSV files, parsing dates
load = pd.read_csv(
    'Data/Realisierter_Stromverbrauch_201811010000_202411010000_Stunde.csv', 
    sep=';', 
    parse_dates=['Datum von', 'Datum bis'],
    dayfirst=True
)
production = pd.read_csv(
    'Data/Realisierte_Erzeugung_201811010000_202411010000_Stunde.csv', 
    sep=';', 
    parse_dates=['Datum von', 'Datum bis'],
    dayfirst=True
)
price = pd.read_csv(
    'Data/Gro_handelspreise_201811010000_202411010000_Stunde.csv', 
    sep=';', 
    parse_dates=['Datum von', 'Datum bis'],
    dayfirst=True
)

# Select relevant date range for all DataFrames
start_date = '2018-11-01'
end_date = '2024-10-31'

load_filtered = load[(load['Datum von'] >= start_date) & (load['Datum bis'] <= end_date)]
production_filtered = production[(production['Datum von'] >= start_date) & (production['Datum bis'] <= end_date)]
price_filtered = price[(price['Datum von'] >= start_date) & (price['Datum bis'] <= end_date)]

# Ensure the merging key is consistent (e.g., use 'Datum von' as the key)
# Rename columns for clarity if needed
load_filtered = load_filtered.rename(columns={'Datum von': 'Date'})
production_filtered = production_filtered.rename(columns={'Datum von': 'Date'})
price_filtered = price_filtered.rename(columns={'Datum von': 'Date'})

# Merge DataFrames on the 'Date' column
merged_df = pd.merge(load_filtered, production_filtered, on='Date', how='outer')
merged_df = pd.merge(merged_df, price_filtered, on='Date', how='outer')

# Display the result
print(merged_df.head())

# Save the merged DataFrame if needed
merged_df.to_csv('Data/merged_data.csv', index=False)
