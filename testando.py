import streamlit as st
import pandas as pd
st.title('Trabalho de programação')
st.caption('lavis')

df = pd.read_csv('Human.csv', sep=',')
st.dataframe(df)
