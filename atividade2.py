import streamlit as st
import pandas as pd
st.title('Trabalho csv e gráfico')
st.caption('Lavínia')

df = pd.read_csv('Human.csv', sep=',')
st.dataframe(df) 
