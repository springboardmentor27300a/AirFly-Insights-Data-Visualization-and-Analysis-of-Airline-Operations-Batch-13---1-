# ✈️ AirFly Insights: Aviation Operational Analysis & Visualization

**Author:** Siddarth V Acharya

---

## 📌 Project Scope

**Domain:** Large-Scale Data Analysis & Visualization
**Dataset:** US DOT Airline Flight Delays *(60M+ Records)*

---

## ✈️ Project Overviewrmdir /s /q .git

**AirFly Insights** is a high-scale data analytics project focused on uncovering operational inefficiencies, delay propagation patterns, and cancellation drivers in the aviation ecosystem.

Using a massive dataset from the **U.S. Department of Transportation**, this project transforms raw flight records into **actionable intelligence** on airline performance, airport congestion, and seasonal variability.

---

## 🎯 Key Objectives

* **Scalability:** Efficiently process and analyze **60+ million records** on commodity hardware
* **Data Analysis:** Identify high-risk routes, congestion windows, and delay propagation patterns
* **Visualization:** Develop intuitive, high-signal dashboards for delay categorization
* **Predictive Readiness:** Build engineered features to support future delay prediction models

---

## 🛠️ Tech Stack

| Category            | Tools / Libraries                       |
| ------------------- | --------------------------------------- |
| **Language**        | Python 3.x                              |
| **Data Processing** | Pandas, NumPy                           |
| **Visualization**   | Matplotlib, Seaborn, Plotly             |
| **Environment**     | Jupyter Notebook                        |
| **Data Ingestion**  | KaggleHub                               |
| **Optimization**    | Memory Downcasting, Sampling Techniques |

---

## 📈 Project Milestones

### 🔹 Milestone 1: Data Foundations & Optimization

* **Automated Ingestion:** Integrated `kagglehub` for seamless dataset retrieval
* **Memory Optimization:** Reduced memory usage by **>40%** using type downcasting (`float64 → float32`)
* **Data Cleaning:**

  * Handled missing values in delay attributes
  * Standardized temporal fields
* **Feature Engineering:**

  * `FL_DATE` (datetime conversion)
  * `DEP_HOUR` (hour-based segmentation)
  * `ROUTE` (Origin–Destination mapping)

---

### 🔹 Milestone 2: Exploratory Data Analysis

* **Market Share Analysis:**
  Identified **Top 10 airlines** and busiest hubs *(ATL, ORD, DFW)*

* **Correlation Studies:**
  Examined relationship between **distance vs. arrival delay**

* **Temporal Trends:**
  Revealed **delay accumulation effect** during evening peak hours

---

### 🔹 Milestone 3: Route & Seasonal Insights

* **High-Risk Route Detection:**
  Identified routes with elevated cancellation probability

* **Cancellation Analysis:**
  Categorized delays into:

  * Carrier
  * Weather
  * Security
  * NAS (National Aviation System)

* **Seasonality Impact:**
  Highlighted winter disruptions and holiday surge effects

---

### 🔹 Milestone 4: Reporting & Synthesis

* **Dashboard Development:**
  Consolidated multi-dimensional insights into cohesive visuals

* **KPI Tracking:**
  Defined baseline metrics for **On-Time Performance (OTP)**

* **Final Deliverables:**

  * Technical documentation
  * Presentation-ready insights
  * Structured analytical pipeline

---

## 🚀 Key Insights

* **Delay Propagation (Ripple Effect):**
  Late aircraft delays are the **primary driver of cascading delays**, especially in evening schedules

* **Hub Bottlenecks:**
  A disproportionate share of delays originates from **major hub congestion**

* **Weather Impact:**
  While less frequent, **weather-related cancellations** cause the **highest disruption severity**, particularly in Q4

---


## 🔧 How to Run


### 3 Execute the Pipeline

Start with:

```bash
notebooks/milestone.ipynb
```

Then proceed sequentially through the notebooks.

---

## 📎 License

This project is licensed under the **MIT License**

---

## ⭐ Final Note

This project demonstrates **end-to-end large-scale data analytics**, combining **data engineering, visualization, and analytical reasoning** to extract meaningful insights from complex aviation datasets.

---
