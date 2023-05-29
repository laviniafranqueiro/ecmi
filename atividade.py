import streamlit as 
import pandas as pd 
st.title('tarefa do Josir')
st.caption('Lavínia Franqueiro')

df = pd.read_csv('marijuana.csv', sep =';')
st.dataframe(df)

#arquivo = open('marijuana.csv')
#for linha in arquivo:
#    st.write(linha)
