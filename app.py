import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('Data/vehicles.csv')

# Header
st.header("Car Sales Analysis")

# --- Histogram Checkbox ---
build_histogram = st.checkbox('Show histogram for "price"')

if build_histogram: # creating a selection box
    st.write("creating histogram...")
    fig_hist = px.histogram(df, x='price',nbins=50, title='Price Distribution')
    st.plotly_chart(fig_hist, use_container_width=True)

# --- Scatter Plot Checkbox ---
build_scatter = st.checkbox('Show scatter plot (odometer vs price)')

if build_scatter: # creating a selection box
    st.write("creating scatter plot...")
    fig_scatter = px.scatter(
        df,
        x='odometer',
        y='price',
        title='Price vs Odometer',
        opacity=0.5
    )
    st.plotly_chart(fig_scatter,use_container_width=True)

