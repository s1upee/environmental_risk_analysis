import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Check available columns
df_preview = pd.read_csv("data/resultphyschem.csv", nrows=1000, low_memory=False)
print(df_preview.columns)
print(df_preview.head())

# Step 2: Load only needed columns
use_cols = ["ActivityStartDate", "ResultMeasureValue", "CharacteristicName", "ActivityLocation/LatitudeMeasure", "ActivityLocation/LongitudeMeasure"]
df = pd.read_csv("data/resultphyschem.csv", usecols=use_cols, low_memory=False)

# Step 3: Filter pollutants
df = df[df['CharacteristicName'].str.contains("Lead|Nitrate|E. coli", case=False, na=False)]
df['ResultMeasureValue'] = pd.to_numeric(df['ResultMeasureValue'], errors='coerce')
df = df.dropna(subset=['ResultMeasureValue'])

# Step 4: Overview & Hist Plot
print(df.describe())
plt.figure(figsize=(8, 5))
df['ResultMeasureValue'].hist(bins=50)
plt.title("Distribution of Result Measure Values (Florida)")
plt.savefig("outputs/Lead_Distribution_Florida.png")
plt.close()

# Step 5: Date conversion and grouping
df['ActivityStartDate'] = pd.to_datetime(df['ActivityStartDate'])

grouped = df.groupby(['CharacteristicName'])['ResultMeasureValue'].mean().reset_index()
print(grouped.sort_values(by='ResultMeasureValue', ascending=False))

# Step 6: Top pollutants in Florida
plt.figure(figsize=(10, 6))
sns.barplot(data=grouped, x='ResultMeasureValue', y='CharacteristicName', palette='Reds')
plt.title("Average Pollutant Concentrations in Florida")
plt.xlabel("Avg Concentration (mg/L)")
plt.ylabel("Pollutant")
plt.tight_layout()
plt.savefig("outputs/Top_Pollutants_Florida.png")
plt.close()

# Step 7: Lead over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=df[df['CharacteristicName'] == 'Lead'],
             x='ActivityStartDate', y='ResultMeasureValue')
plt.title("Lead Concentration Over Time in Florida")
plt.ylabel("Concentration (mg/L)")
plt.xlabel("Date")
plt.tight_layout()
plt.savefig("outputs/Lead_Over_Time_Florida.png")
plt.close()

# Step 8: Nitrate geospatial spread
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df[df['CharacteristicName'] == 'Nitrate'],
    x='ActivityLocation/LongitudeMeasure',
    y='ActivityLocation/LatitudeMeasure',
    hue='ResultMeasureValue',
    palette='coolwarm'
)
plt.title("Geographic Spread of Nitrate Levels in Florida")
plt.tight_layout()
plt.savefig("outputs/Nitrate_Spread_Florida.png")
plt.close()
