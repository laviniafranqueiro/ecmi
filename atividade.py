import streamlit as st
import pandas as pd 
import csv
st.title('tarefa do Josir')
st.caption('Lavínia Franqueiro')

df = pd.read_csv('acidentes.csv', sep =',')
st.dataframe(df)

#arquivo = open('acidentes.csv')
#for linha in arquivo:
#    st.write(linha)
