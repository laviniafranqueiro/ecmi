import streamlit as st
import pandas as pd

st.title("articles(1).csv")

csv_file = st.file_uploader("articles(1).csv", type=["csv"])

if csv_file is not None:
    df = pd.read_csv(csv_file)
    st.write(df)
