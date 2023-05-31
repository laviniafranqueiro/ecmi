import streamlit as st
import pandas as pd 
st.title('tarefa do Josir')
st.caption('Lavínia Franqueiro')

df = pd.read_csv('acidentes.csv', sep =',')
st.dataframe(df)

chart_data = df[['Road Accidents during 2018', 'Road Accidents during 2019', 'Road Accidents during 2020']]
st.line_chart(chart_data)
