import streamlit as st
import pandas as pd

st.header('st.file_uploader')

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  with st.subheader('DataFrame'):
    st.write(df)
  with st.subheader('Descriptive Statistics'):
    st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
