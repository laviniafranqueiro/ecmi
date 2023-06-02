import streamlit as st
import pandas as pd
import numpy as np

st.title('Teste ECMI 2')

st.write("Tabela")

lista_salario = [10000,15000,490,7688]
lista_nomes = ['Josir', 'Bruno', 'Bruna', 'Anna']

texto = st.text_input("Digite um nome") 
salario = float(st.text_input("Digite um salario", "0"))

dataframe = pd.DataFrame({
    'Nome': lista_nomes,
    'Salário': lista_salario
})

dataframe.style.highlight_max(axis=0)

st.write(dataframe)

chart_data = pd.DataFrame(
     np.random.randn(20,3),
     columns=['a','b','c'])

st.line_chart(chart_data)
