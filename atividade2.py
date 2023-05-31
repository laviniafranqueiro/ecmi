import streamlit as st
import pandas as pd 
st.title('tarefa do Josir')
st.caption('Lavínia Franqueiro')

df = pd.read_csv('Human.csv', sep =',')
st.dataframe(df)

chart_data = df[['Human development Index (HDI)', 'Life expectancy at birth', 'Expected years of schooling']]
st.line_chart(chart_data)
