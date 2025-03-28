import streamlit as st
import pandas as pd
import src.get_data as get_data
import src.widgets as meine_widgets
import plotly.express as px

df = get_data.lade_bevoelkerung_entwicklung()

meine_widgets.get_abs_rel()
meine_widgets.get_timeline(2000)

df_von = df.query(f"Jahr == {st.session_state["Jahr_von"]}")
df_bis = df.query(f"Jahr == {st.session_state["Jahr_bis"]}")
df_trend = pd.merge(left=df_von,
                    right=df_bis,
                    on="Land",
                    suffixes=["_von", "_bis"])

df_trend["Wachstum"] = ((df_trend["Bevoelkerung_bis"] - df_trend["Bevoelkerung_von"]) / 1000 if st.session_state["abs/rel"] == "absolut" 
                        else df_trend["Bevoelkerung_bis"] / df_trend["Bevoelkerung_von"] * 100)



df_out = (df_trend[["Land", "Wachstum"]]
          .sort_values(by="Wachstum",
                       ascending=False).iloc[:10][::-1])

if st.session_state["abs/rel"] == "absolut":
    x_label = "Wachstum in Mio"
    text_format = "%{x:.0f} Mio"
else:
    x_label = "Wachstum in %"
    text_format = "%{x:.0f} %"

bar_chart = px.bar(df_out,
                   x="Wachstum",
                   y="Land",
                   title="Top 10 Länder mit dem stärksten Wachstum",
                   orientation="h")

bar_chart.update_layout(xaxis_title=x_label,
                        yaxis_title=None)
bar_chart.update_traces(texttemplate=text_format,
                        textposition="inside")

st.plotly_chart(bar_chart)

meine_widgets.get_quelle()