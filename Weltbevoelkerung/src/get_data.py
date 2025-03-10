import os
import pickle
import pandas as pd


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FILE_PATH_BEVOELK = os.path.join(BASE_DIR, "data", "bevoelkerung.pkl")

def load_saved_data():
    with open(FILE_PATH_BEVOELK, "rb") as input:
        df = pickle.load(input)
    
    return df


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
    
    with open(FILE_PATH_BEVOELK, "wb") as output:
        pickle.dump(df, output)
