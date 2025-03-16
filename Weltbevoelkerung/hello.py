import streamlit as st
import pandas as pd
import src.get_data as get_data
import plotly.express as px

entwicklung_page = st.Page(page = "pages/bevoelkerung_entwicklung_laender.py",
                           title="Bevölkerungsentwicklung",
                           icon="📈",
                           url_path="bevoelkerungsentwicklung")

gesamt_page = st.Page(page = "pages/bevoelkerung_gesamt.py",
                      title="Weltbevölkerung",
                      icon="🌍",
                      url_path="weltbevoelkerung")

pg = st.navigation([entwicklung_page, gesamt_page])
pg.run()
