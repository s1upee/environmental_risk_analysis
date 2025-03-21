import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
aqi_county = pd.read_csv("annual_aqi_by_county_2024.csv")
aqi_cbsa = pd.read_csv("annual_aqi_by_cbsa_2024.csv")
pollution_monitor = pd.read_csv("annual_conc_by_monitor_2024.csv")

# View basic info
print(aqi_county.info())
print(aqi_county.head())

# Summary statistics
print(aqi_county.describe())

# Unique states and counties
print(aqi_county["State"].unique())
print(aqi_county["County"].unique())

# Check for missing values
print(aqi_county.isnull().sum())

# Compute average AQI by state
aqi_by_state = aqi_county.groupby("State")["Max AQI"].mean().sort_values(ascending=False)
print(aqi_by_state)

# Compute overall AQI distribution
print(aqi_county["Max AQI"].describe())

# Example: Compare AQI of California (industrial) vs. Montana (rural)
industrial_states = ["California", "Texas", "New York"]
rural_states = ["Montana", "Wyoming", "Vermont"]

# Define selected states and filter the DataFrame
selected_states = industrial_states + rural_states
filtered_aqi = aqi_county[aqi_county["State"].isin(selected_states)]

# Create a boxplot
plt.figure(figsize=(12,6))
sns.boxplot(data=filtered_aqi, x="State", y="Max AQI", order=selected_states, palette="coolwarm")
plt.title("AQI Distribution: Industrial vs. Rural States (2024)")
plt.xlabel("State")
plt.ylabel("Max AQI")
plt.xticks(rotation=45)
plt.show()

industrial_aqi = aqi_county[aqi_county["State"].isin(industrial_states)].groupby("State")["Max AQI"].mean()
rural_aqi = aqi_county[aqi_county["State"].isin(rural_states)].groupby("State")["Max AQI"].mean()

print("Industrial Areas AQI:\n", industrial_aqi)
print("Rural Areas AQI:\n", rural_aqi)

# Bar chart of AQI by state
plt.figure(figsize=(12,6))
aqi_by_state.head(15).plot(kind="bar", color="red")
plt.title("Top 15 States with Highest AQI (2024)")
plt.ylabel("Max AQI")
plt.xticks(rotation=45)
plt.show()

# Find most common pollutants
print(pollution_monitor["Parameter Name"].value_counts())

# Compare pollution levels by pollutant
pollutant_levels = pollution_monitor.groupby("Parameter Name")["Arithmetic Mean"].mean()
print(pollutant_levels)

plt.figure(figsize=(14,6))  # Increase figure width
top_pollutants = pollutant_levels.sort_values(ascending=False).head(10)  # Show only top 10
sns.barplot(x=top_pollutants.index, y=top_pollutants.values, palette="viridis")
plt.title("Top 10 Pollutants by Average Concentration (2024)")
plt.ylabel("Mean Concentration")
plt.xlabel("Pollutant Name")
plt.xticks(rotation=30, ha='right')  # Better label readability
plt.yscale("log")  # If concentration varies widely
plt.show()
