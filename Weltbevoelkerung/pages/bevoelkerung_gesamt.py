import streamlit as st
import pandas as pd
import src.get_data as get_data
import src.widgets as meine_widgets
import plotly.express as px

df = get_data.lade_bevoelkerung_gesamt()

st.header("Weltbevölkerung seit 1950")

meine_widgets.get_timeline()

df_filtered = df.query(f"Jahr >= {st.session_state["Jahr_von"]} and Jahr <= {st.session_state["Jahr_bis"]}")

line_chart = px.line(data_frame=df_filtered,
                     x=df_filtered.index,
                     y="Bevölkerung")

st.plotly_chart(line_chart)

meine_widgets.get_quelle()