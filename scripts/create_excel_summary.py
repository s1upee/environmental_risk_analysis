import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("data/annual_conc_by_monitor_2024.csv", low_memory=False)
print(df.columns)
print(df['Parameter Name'].unique())

# Step 2: Keep only the important columns
columns_to_keep = [
    'State Name',
    'County Name',
    'Parameter Name',
    'Arithmetic Mean',
    '1st Max Value',
    'Units of Measure'
]
df_small = df[columns_to_keep]

# Step 3: Filter for key pollutants
# You can change this list if you want to focus on others
pollutants = ['Lead (TSP) LC', 'Volatile Organic Compounds', 'Hazardous Air Pollutants']
df_filtered = df_small[df_small['Parameter Name'].isin(pollutants)]

# Step 4: Group and summarize the data
df_summary = df_filtered.groupby(['State Name', 'Parameter Name']).agg({
    'Arithmetic Mean': 'mean',
    '1st Max Value': 'max'
}).reset_index()

# Rename columns for clarity in Excel
df_summary.rename(columns={
    'State Name': 'State',
    'Parameter Name': 'Pollutant',
    'Arithmetic Mean': 'Avg Concentration',
    '1st Max Value': 'Max Value'
}, inplace=True)

# Step 5: Export to Excel
output_path = "EHS_pollution_dashboard.xlsx"
df_summary.to_excel(output_path, sheet_name="Raw_Data", index=False)

print(f"✅ Excel summary saved as: {output_path}")
