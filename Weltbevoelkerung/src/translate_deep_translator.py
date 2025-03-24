import pickle
from deep_translator import GoogleTranslator

# Lade DataFrame aus Pickle-File
with open("../data/dataframe.pkl", "rb") as input:
    df = pickle.load(input)

# Erstelle Liste aller Länder, damit die (rechenintensive) Übersetzungsfunktion möglichst selten aufgerufen wird
# Für 237 Länder arbeitet der Translator etwa 1 Minute
alle_laender = df["Land"].unique()

# Erstelle ein Dictionary mit dem alten und dem neuen Wert
uebersetzung = dict()
for land in alle_laender:
    uebersetzung.update({land: GoogleTranslator(source="en", target="de").translate(land)})

# Ersetze die englischen Werte durch die deutschen
df["Land"] = df["Land"].replace(uebersetzung)

# Et voilà!
with open("../data/dataframe.pkl", "wb") as output:
    pickle.dump(df, output)
