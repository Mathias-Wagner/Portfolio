import streamlit as st
import src.get_data as get_data

jahr_min_max = get_data.lade_jahr_min_max()

def get_timeline(default_von: int=jahr_min_max[0]):
    st.session_state["Jahr_von"], st.session_state["Jahr_bis"] = st.slider(label="Zeitraum",
                                                                           min_value=jahr_min_max[0],
                                                                           max_value=jahr_min_max[1],
                                                                           value=[default_von, jahr_min_max[1]])


def get_abs_rel():
    st.session_state["abs/rel"] = st.radio(label="Verändung",
                                           options=["absolut", "relativ"],
                                           horizontal=True)
    

def __get_laender():
    laender = list(get_data.lade_geschlechterverteilung()["Land"].unique())
    laender.sort()
    laender.remove("Welt")
    laender.remove("Deutschland")
    laender.remove("Österreich")
    laender.remove("Schweiz")
    laender.insert(0, "Schweiz")
    laender.insert(0, "Österreich")
    laender.insert(0, "Deutschland")
    laender.insert(0, "Welt")
    
    return laender
    

def get_dropdown_laender():
    laender = __get_laender()
    st.session_state["land"] = st.selectbox(label="Land",
                                            options=laender)


def get_quelle():
    col1, col2 = st.columns([.65, .35])
    col2.markdown("Quelle: [UN Population Division](https://population.un.org/wpp/assets/Excel%20Files/1_Indicator%20(Standard)/EXCEL_FILES/1_General/WPP2024_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT.xlsx) \n \
    (zuletzt abgerufen am 16.03.2025)",
    unsafe_allow_html=False)