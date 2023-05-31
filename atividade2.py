import streamlit as 
import pandas as pd 
import csv
st.title('trabalho csv')
st.caption('Lavínia Franqueiro')

df = pd.read_csv('acidentes.csv', sep =';')
st.dataframe(df)
