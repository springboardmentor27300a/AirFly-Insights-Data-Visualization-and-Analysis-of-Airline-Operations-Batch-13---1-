import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("AirFly Insights Dashboard")
st.write("Airline Operations Data Visualization")

# Load dataset
df = pd.read_csv("flights_cleaned_full.csv")

# Sidebar filters
st.sidebar.header("Filters")

airline = st.sidebar.selectbox(
    "Select Airline",
    df["AIRLINE"].unique()
)

filtered_df = df[df["AIRLINE"] == airline]

# Flights by Month
st.subheader("Flights by Month")
month_counts = filtered_df["MONTH_NAME"].value_counts()

fig1, ax1 = plt.subplots()
sns.barplot(x=month_counts.index, y=month_counts.values, ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# Delay by Hour
st.subheader("Average Delay by Hour")
hour_delay = filtered_df.groupby("DEP_HOUR")["ARRIVAL_DELAY"].mean()

fig2, ax2 = plt.subplots()
sns.lineplot(x=hour_delay.index, y=hour_delay.values, ax=ax2)
st.pyplot(fig2)

# Airport Delay Map
st.subheader("Airport Delay Map")

airport_delay = df.groupby('ORIGIN_AIRPORT')['DEPARTURE_DELAY'].mean().reset_index()

airports = pd.read_csv("airports.csv")

airport_map = pd.merge(
    airport_delay,
    airports,
    left_on='ORIGIN_AIRPORT',
    right_on='IATA_CODE',
    how='left'
)

airport_map['DELAY_SIZE'] = airport_map['DEPARTURE_DELAY'].abs()
airport_map = airport_map.dropna(subset=['LATITUDE','LONGITUDE'])

fig = px.scatter_geo(
    airport_map,
    lat='LATITUDE',
    lon='LONGITUDE',
    size='DELAY_SIZE',
    color='DEPARTURE_DELAY',
    hover_name='ORIGIN_AIRPORT',
    scope='usa'
)

st.plotly_chart(fig)

# Cancellation Trends
st.subheader("Monthly Cancellation Trends")

cancel_month = df.groupby('MONTH_NAME')['CANCELLED'].sum()

fig3, ax3 = plt.subplots()
sns.barplot(x=cancel_month.index, y=cancel_month.values, ax=ax3)
plt.xticks(rotation=45)
st.pyplot(fig3)