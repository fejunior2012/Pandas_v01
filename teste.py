import pandas as pd
from datetime import datetime
import streamlit as st

caminho_csv_anderson = r'C:\Users\r244817\GitHub\Pandas_v01\funcionarios.csv'
df = pd.read_csv(caminho_csv_anderson, sep=";")

st.write(df)

df["Data de Nascimento"] = pd.to_datetime(df["Data de Nascimento"], format="%d/%m/%Y")
st.write(df)

print(df.info())

print()
