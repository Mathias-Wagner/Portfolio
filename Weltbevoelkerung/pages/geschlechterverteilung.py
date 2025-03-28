import streamlit as st
import pandas as pd
import src.get_data as get_data
import src.widgets as meine_widgets
import plotly.express as px

df = get_data.lade_geschlechterverteilung().drop(columns=["Bevoelkerung"])

meine_widgets.get_dropdown_laender()

st.text(st.session_state["land"])

df = pd.melt(df, id_vars=["Land", "Jahr"], var_name="Geschlecht", value_name="Anzahl")
df = df.query(f"Land == '{st.session_state["land"]}'")
df = df.replace("Maenner", "Männer")

line_chart = px.line(df,
                     x="Jahr",
                     y="Anzahl",
                     color="Geschlecht")

st.plotly_chart(line_chart)

meine_widgets.get_quelle()