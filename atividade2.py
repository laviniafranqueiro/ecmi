import streamlit as st
import pandas as pd
st.title('Trabalho csv e gráfico')
st.caption('Lavínia')

df = pd.read_csv('acidentes.csv', sep=';')
st.dataframe(df) 
