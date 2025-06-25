import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("true_cost_fast_fashion.csv")

st.header("Fast Fashion Production Analysis")


st.sidebar.title("Filter Options")

# Filter by Country
countries = df['Country'].unique()
selected_countries = st.sidebar.multiselect(
    "Select Countries", options=countries, default=countries[0])
# Filter by Brand
brands = df['Brand'].unique()
selected_brands = st.sidebar.multiselect(
    "Select Brands", options=brands, default=brands)
# Filter by Year
years = df['Year'].unique()
selected_years = st.sidebar.slider(
    "Select Years", min_value=int(years.min()),
    max_value=int(years.max()), value=(int(years.min()), int(years.max())),
    step=1)

# main columns
col1, col2 = st.columns(2)

# Filter the DataFrame based on selections
filtered_df = df[
    (df['Country'].isin(selected_countries)) & 
    (df['Brand'].isin(selected_brands)) &
    (df['Year'].between(selected_years[0], selected_years[1]))]

# Create a pivot table for production data
pivot = filtered_df.pivot_table(index='Year',
                                columns='Brand',
                                values=['Monthly_Production_Tonnes','GDP_Contribution_Million_USD'],
                                aggfunc='sum').reset_index()
# Flatten the MultiIndex columns
pivot.columns = [' '.join(col).strip() if isinstance(col, tuple) else col for col in pivot.columns]


col1.subheader("Production Over Time")
# Create a line chart for production data
fig_prod = px.line(pivot, x="Year", y=[col for col in pivot.columns if 'Monthly_Production_Tonnes' in col],
                   title="Monthly Production by Brand Over Time")
col1.plotly_chart(fig_prod)

col2.subheader("GPD Contribution Over Time")
fig_prod = px.line(pivot, x="Year", y=[col for col in pivot.columns if 'GDP_Contribution_Million_USD' in col],
                   title="GPD Contribution Over Time")
col2.plotly_chart(fig_prod)
