import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

haps = pd.read_csv("data/daily_HAPS_2024/daily_HAPS_2024.csv", low_memory=False)
vocs = pd.read_csv("data/daily_VOCS_2024/daily_VOCS_2024.csv", low_memory=False)
lead = pd.read_csv("data/daily_LEAD_2024/daily_LEAD_2024.csv", low_memory=False)

print(haps.columns)
print(vocs.columns)
print(lead.columns)

haps = haps.rename(columns={"Arithmetic Mean": "HAPs"})
vocs = vocs.rename(columns={"Arithmetic Mean": "VOCs"})
lead = lead.rename(columns={"Arithmetic Mean": "Lead"})

haps['Date'] = pd.to_datetime(haps['Date Local'])
vocs['Date'] = pd.to_datetime(vocs['Date Local'])
lead['Date'] = pd.to_datetime(lead['Date Local'])

haps = haps[['Date', 'State Code', 'County Code', 'Site Num', 'HAPs']]
vocs = vocs[['Date', 'State Code', 'County Code', 'Site Num', 'VOCs']]
lead = lead[['Date', 'State Code', 'County Code', 'Site Num', 'Lead']]

merged = haps.merge(vocs, on=['Date', 'State Code', 'County Code', 'Site Num'])
merged = merged.merge(lead, on=['Date', 'State Code', 'County Code', 'Site Num'])

print(merged.describe())
print(merged.isnull().sum())

by_region = merged.groupby(['State Code', 'County Code'])[['HAPs', 'VOCs', 'Lead']].mean().reset_index()
by_region = by_region.sort_values(by='HAPs', ascending=False)
print(by_region.head(10))  # Show top-10 most polluted counties by HAPs

sns.heatmap(merged.corr(), annot=True)
plt.title("Correlation Between Pollutants")
plt.savefig("outputs/Correlation_Between_Pollutants.png")
plt.show()

# Top 10 counties by average HAPs
top10 = by_region.head(10)
plt.figure(figsize=(10,6))
sns.barplot(data=top10, x='HAPs', y='County Code', hue='State Code')
plt.title("Top 10 Counties with Highest Average HAPs")
plt.savefig("outputs/Top10_Counties_HAPs.png")
plt.show()