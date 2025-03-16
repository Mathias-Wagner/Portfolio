import os
import pickle
import pandas as pd


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
__FILE_PATH_BEVOELK_GESAMT = os.path.join(BASE_DIR, "data", "bevoelkerung.pkl")
__FILE_PATH_BEVOELK_ENTWICKLUNG = os.path.join(BASE_DIR, "data", "bevoelkerungsentwicklung.pkl")
__FILE_PATH_JAHR_MIN_MAX = os.path.join(BASE_DIR, "data", "jahr_min_max.pkl")

def __lade_dataframe(file_path):
    with open(file_path, "rb") as input:
        df = pickle.load(input)

    return df


def lade_bevoelkerung_gesamt():
    return __lade_dataframe(__FILE_PATH_BEVOELK_GESAMT)


def lade_bevoelkerung_entwicklung():
    return __lade_dataframe(__FILE_PATH_BEVOELK_ENTWICKLUNG)


def lade_jahr_min_max():
    with open(__FILE_PATH_JAHR_MIN_MAX, "rb") as input:
        jahr_min_max = pickle.load(input)
        
    return jahr_min_max


def update_data():
    df = pd.read_excel("https://population.un.org/wpp/assets/Excel%20Files/1_Indicator%20(Standard)/EXCEL_FILES/1_General/WPP2024_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT.xlsx",
                       skiprows=16)
    
    columns = {"Year": "Jahr",
               "Total Population, as of 1 January (thousands)": "Bevölkerung"}
    
    df = (df
          .query("Type == 'World'")[columns.keys()]
          .rename(columns=columns)
          .astype({"Jahr": "int"})
          .set_index("Jahr"))
    
    df.loc[:, "Bevölkerung"] = df.loc[:, "Bevölkerung"] * 1000
    
    with open(__FILE_PATH_BEVOELK_GESAMT, "wb") as output:
        pickle.dump(df, output)
