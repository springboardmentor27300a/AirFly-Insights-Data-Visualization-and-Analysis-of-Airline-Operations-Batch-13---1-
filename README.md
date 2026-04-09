# ✈️ AirFly Insights
### Data Visualization and Analysis of Airline Operations

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-1.x-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=flat-square&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75?style=flat-square&logo=plotly&logoColor=white)](https://plotly.com)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)](https://jupyter.org)

> Uncovering delay patterns, cancellation trends, and operational insights from **5.8 million** US flight records through end-to-end data visualization.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Key Findings](#-key-findings)
- [Dataset](#-dataset)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Milestones](#-milestones)
- [KPI Metrics](#-kpi-metrics)
- [Visualizations](#-visualizations)
- [Getting Started](#-getting-started)
- [Author](#-author)

---

## 🔍 Project Overview

**AirFly Insights** is a comprehensive data analysis and visualization project that explores large-scale US airline operations data. The goal is to identify delay drivers, cancellation patterns, seasonal trends, and route-level congestion — providing actionable insights for airline operators, analysts, and aviation stakeholders.

**Core objectives:**
- Preprocess and engineer features from raw aviation data
- Explore trends in schedules, delays, cancellations, and routes
- Visualize key metrics using bar charts, heatmaps, time series, and maps
- Build an interactive Power BI dashboard for stakeholder reporting

---

## 💡 Key Findings

| # | Insight |
|---|---------|
| 🏆 | **WN (Southwest Airlines)** operates the highest number of flights |
| ⏱️ | **Late aircraft delay** is the single largest delay contributor across all airlines |
| 🌙 | **Evening hours (6–8 PM)** show peak delay rates; morning flights are most on-time |
| ❄️ | **Winter months** (Dec–Feb) account for **40,562 cancellations** |
| 🌦️ | **Weather** is the primary reason for flight cancellations |
| 🛫 | **SFO → LAX** is the busiest domestic route |
| 📅 | **Friday** is the busiest day of the week for flight operations |
| 📊 | Overall **on-time performance: 64.14%** |

---

## 📦 Dataset

| Property | Value |
|----------|-------|
| **Source** | [Kaggle — Airlines Flights Data](https://www.kaggle.com/datasets/usdot/flight-delays) |
| **Total Records** | 5.8 Million flights |
| **Total Airlines** | 14 |
| **Original Columns** | 31 |
| **Engineered Features** | +3 (`ROUTE`, `MONTH_NAME`, `DEPARTURE_HOUR`) |

**Key columns used:**
`AIRLINE` · `ORIGIN_AIRPORT` · `DESTINATION_AIRPORT` · `DEPARTURE_DELAY` · `ARRIVAL_DELAY` · `CANCELLATION_REASON` · `WEATHER_DELAY` · `LATE_AIRCRAFT_DELAY` · `AIR_SYSTEM_DELAY` · `CARRIER_DELAY` · `MONTH` · `DAY_OF_WEEK`

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| **Data Handling** | `pandas`, `numpy` |
| **Visualization** | `matplotlib`, `seaborn`, `plotly`, `folium` |
| **Dashboard** | Power BI |
| **Preprocessing** | Python, Excel |
| **Notebook** | Jupyter Notebook |
| **Version Control** | Git, GitHub |

---

## 📁 Project Structure

```
airfly-insights/
│
├── data/
│   ├── raw/                    # Original Kaggle dataset
│   └── processed/              # Cleaned & feature-engineered data
│
├── notebooks/
│   └── AirFly_Insights--Data_Visualization_and_Analysis_of_Airline_Operations.ipynb   # Main analysis notebook
│
├── dashboard/
│   └── AirFly_Dashboard.pbix   # Power BI dashboard file or ScreenShots
│
├── reports/
│   └── All Milestones Final PPT.pptx
│
└── README.md
```

---

## 🚀 Milestones

### Milestone 1 — Data Foundation & Cleaning
> **Weeks 1–2**

- Loaded 5.8M records from CSV using pandas with memory optimization
- Removed fully empty rows and duplicate records
- Handled missing values:
  - Delay columns → filled with `0` (standard for non-delayed flights)
  - `AIR_TIME`, `ELAPSED_TIME`, `TAXI_IN`, `TAXI_OUT` → filled with **median**
- Engineered 3 new features: `ROUTE`, `MONTH_NAME`, `DEPARTURE_HOUR`
- Standardized date column format
- Final dataset: **5.8M rows × 31 columns**

---

### Milestone 2 — Visual Exploration & Delay Trends
> **Weeks 3–4**

Produced **8+ visualizations** covering:

- 📊 Top airlines and routes by flight volume
- 📅 Monthly, daily, and hourly flight distributions
- 🏢 Busiest airports by traffic
- ⏱️ Delay causes: carrier, weather, NAS, late aircraft, security
- 🕐 Arrival delay by departure hour (morning vs. evening patterns)

**Conclusion:** Evening hours and late aircraft delays are the primary operational challenges.

---

### Milestone 3 — Route, Cancellation & Seasonal Insights
> **Weeks 5–6**

- Identified **Top 10 origin-destination pairs** by volume
- Built delay heatmaps by airport and delay type
- Analyzed monthly cancellation trends with seasonal breakdowns
- Studied winter impact: **40,562 cancellations** in Dec–Feb
- Found strong correlation between high delays and cancellations

**Conclusion:** Weather and aircraft operations are the dominant disruption factors.

---

### Milestone 4 — Dashboard & Final Report
> **Weeks 7–8**

- Built interactive **Power BI dashboard** with KPI cards, filters, and drill-down views
- Dashboard filters: Airline · Origin · Destination · Month · Day of Week
- Created final slide deck and documentation
- Uploaded code, visuals, and reports to GitHub

---

## 📈 KPI Metrics

```
┌─────────────────────────────────┬───────────────┐
│  Total Flights                  │  5.82 Million │
│  Total Airlines                 │  14           │
│  Avg Departure Delay            │  9.23 min     │
│  Avg Arrival Delay              │  4.33 min     │
│  On-Time Flight Rate            │  64.14%       │
│  Total Winter Cancellations     │  40,562       │
└─────────────────────────────────┴───────────────┘
```

---

## 📊 Visualizations

The following chart types were used throughout the project:

- **Bar Charts** — airline/route/airport comparisons
- **Line Plots** — monthly and hourly flight/delay trends
- **Histograms** — delay distribution analysis
- **Boxplots** — airline-level delay spread comparison
- **Heatmaps** — delay type vs. airport matrix
- **Maps (Folium)** — geographic airport traffic visualization
- **Power BI Dashboard** — interactive KPI and filter-driven report

---

## 👤 Author

**KATAKAM BHARGAVI**  
Data Analytics Project | Andhra Pradesh, India

---

*AirFly Insights — Turning flight data into operational clarity.*
