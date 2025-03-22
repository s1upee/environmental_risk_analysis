## 📁 Large Dataset Storage

Due to GitHub’s file size restrictions, large datasets used in this project are stored externally on Google Drive.

You can access them here:  
🔗 [Environmental Risk Analysis Datasets (Google Drive)](https://drive.google.com/drive/folders/1BlGL7_Ox9wynv0ihNV6qp8GFndNqJ75A?usp=drive_link)

---

### 📚 Dataset Overview & Project Ideas

#### 1. 📊 **Data Analysis & Visualization**
Use annual summaries to explore long-term trends and spatial comparisons.

**Files:**
- `annual_conc_by_monitor_2024.csv` — air pollutant concentration data
- `annual_aqi_by_cbsa_2024.csv` — AQI data by metro area
- `annual_aqi_by_county_2024.csv` — AQI data by county

**Why?** → Analyze trends, visualize air quality changes, and compare regions.

---

#### 2. 📈 **Time-Series Analysis & Forecasting**
Work with high-resolution daily data to train forecasting models and reveal temporal trends.

**Files:**
- `daily_44201_2024.csv` — Ozone (O₃) levels
- `daily_88101_2024.csv` — PM2.5 particulate matter
- `daily_TEMP_2024.csv` — Temperature

**Why?** → Apply time-series models, detect seasonality, and predict pollution levels.

---

#### 3. 🌦️ **Meteorological Influence on Air Quality**
Merge weather and pollution data to explore how climate affects air quality.

**Files:**
- `daily_TEMP_2024.csv` — Temperature
- `daily_WIND_2024.csv` — Wind speed
- `daily_PRESS_2024.csv` — Atmospheric pressure
- `daily_RH_DP_2024.csv` — Relative humidity & dew point

**Why?** → Combine datasets to train regression models linking weather conditions to pollution.

---

#### 4. 🏥 **Pollution and Public Health**
Assess public health risks by analyzing the most toxic pollutants and their regional impact.

**Files:**
- `daily_HAPS_2024.csv` — Hazardous Air Pollutants (HAPs)
- `daily_VOCS_2024.csv` — Volatile Organic Compounds (VOCs)
- `daily_LEAD_2024.csv` — Lead concentrations

**Why?** → Identify regional vulnerabilities and communicate impact through visuals.

### 5. Public Health & Water Pollution (2024)

This analysis focuses on contaminants found in surface water across Florida, using EPA’s `resultphyschem.csv` dataset. Key steps included filtering valid monitoring locations, extracting key pollutants, and identifying substances with the highest average concentrations (e.g., nitrates and lead). The goal was to explore how water quality impacts public health across regions.

📊 Output: Bar chart of top contaminants by average concentration.
📁 Data: `data/resultphyschem.csv`
🧪 Script: `scripts/water_pollution_analysis.py`

---

### 7. Excel Dashboard: Environmental Risk Summary (Lead, 2024)

This Excel-based dashboard was created to support Environmental Health and Safety (EHS) review efforts. Using data from `annual_conc_by_monitor_2024.csv`, it presents key statistics and visualizations for Lead (TSP) levels across U.S. states in 2024.

📁 File: `EHS_pollution_dashboard.xlsx`  
📍 Location: Root directory

**Included Sheets:**
- `Raw_Data`: Cleaned, summarized data by state
- `Dashboard`: Visual insights for risk analysis

**Visualizations:**
- **Top 5 States by Lead Concentration** (bar chart)
- **Average vs Maximum Lead Levels** (clustered column chart)
- *(Optional)* Risk Level Table with conditional formatting

🧠 Purpose: To communicate regional environmental risks using clear visuals and accessible tools for non-technical stakeholders.

> 🚫 Note: Raw data files are ignored in GitHub but available in the linked [Google Drive](https://drive.google.com/drive/folders/1BlGL7_Ox9wynv0ihNV6qp8GFndNqJ75A?usp=drive_link)

---

### 📁 Directory Structure

After downloading, organize the files into the following structure to ensure scripts run correctly:

```
project-root/
├── data/
│   ├── daily_44201_2024/
│   │   └── daily_44201_2024.csv
│   ├── daily_TEMP_2024/
│   │   └── daily_TEMP_2024.csv
│   ├── daily_WIND_2024/
│   │   └── daily_WIND_2024.csv
│   ├── daily_PRESS_2024/
│   │   └── daily_PRESS_2024.csv
│   ├── daily_RH_DP_2024/
│   │   └── daily_RH_DP_2024.csv
│   ├── daily_HAPS_2024/
│   │   └── daily_HAPS_2024.csv
│   ├── daily_VOCS_2024/
│   │   └── daily_VOCS_2024.csv
│   └── daily_LEAD_2024/
│       └── daily_LEAD_2024.csv
```

> ⚠️ Make sure to unzip all files before placing them in their respective folders.

---

## 📩 Contact

If you have any questions, feel free to reach out! 😊  
**Lisa Krasiuk**  
📧 [lisakrasiuk@gmail.com](mailto:lisakrasiuk@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/lisa-krasiuk-84092a302/)
