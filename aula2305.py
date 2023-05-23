import streamlit as st
import pandas as pd
import numpy as np

st.title('Teste ECMI 2')

st.write("Tabela")

dataframe = pd.DataFrame({
    'Nome': ['Josir', 'Bruno', 'Bruna', 'Anna'],
    'Salário': [10000, 15000, 490, 7688]
})
dataframe.style.highlight_max(axis=0)

st.write(dataframe)

chart_data = pd.DataFrame(
     np.random.randn(20,3),
     collumns=['a','b','c'])

st.line_chart(chart_data)
