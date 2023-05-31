import streamlit as st
import pandas as pd 
import csv
st.title('tarefa do Josir')
st.caption('Lavínia Franqueiro')

df = pd.read_csv('acidentes.csv', sep =';')
st.dataframe(df)

chart_data = df[['Road Accidents 2018 ', 'Road Accidents 2019', 'Road Accidents 2020 ']]
st.bar_chart(chart_data)
