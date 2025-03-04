import streamlit as st
import pandas as pd
import src.get_data as get_data
import plotly.express as px

df = get_data.load_saved_data()

st.header("Weltbevölkerung seit 1950")

min_year, max_year = df.index.min(), df.index.max()

year = st.slider(label="Zeitraum",
                 min_value=min_year,
                 max_value=max_year,
                 value=[min_year, max_year])

df_filtered = df.query("Jahr >= @year[0] and Jahr <= @year[1]")

line_chart = px.line(data_frame=df_filtered,
                     x=df_filtered.index,
                     y="Bevölkerung")

st.plotly_chart(line_chart)
