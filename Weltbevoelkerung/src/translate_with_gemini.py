import os
from dotenv import load_dotenv
import pickle
import json
from google import genai

# Get GEMINI API Key from dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
api_key = os.environ.get("GEMINI_API_KEY")

# Lade Daten
with open("../data/bevoelkerung_english.pkl", "rb") as input:
    df = pickle.load(input)

# Erstelle Liste aller Länder und Prompt für Gemini
alle_laender = df["Land"].unique()

prompt = """Übersetze die folgenden Ländernamen in maximal 30 Zeichen ins Deutsche. Verwende die im deutschsprachigen Raum gebräuchlichste Kurzform.
Falls nötig, kürze die Übersetzung weiter, damit du dich an die Begrenzung von 30 Zeichen hältst.
Antworte als JSON-Dictionary mit dem englischen Namen als Schlüssel und der deutschen Übersetzung als Wert:
"""
prompt += json.dumps(list(alle_laender), ensure_ascii=False)

# Öffne Client und schicke Request und verarbeite Response
client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt
)
uebersetzung = json.loads(response.text[8:-4])

# Übersetze Länder im Dataframe
df["Land"] = df["Land"].replace(uebersetzung)

# Speichere Daten
with open("../data/bevoelkerung.pkl", "wb") as output:
    pickle.dump(df, output)
