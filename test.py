import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title("Hello world!")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)

  columns = st.multiselect("Columns:",df.columns)
  filter = st.radio("Choose by:", ("inclusion","exclusion"))

  if filter == "exclusion":
      columns = [col for col in df.columns if col not in columns]

  df = df[columns]
 # x = df[df.columns[0]]
#  y = df[df.columns[1]].sum()
  df = df.groupby([df[df.columns[0]]])[df.columns[1]].sum()
  st.write(df)
 # st.write(x)
 # st.write(y)


  #y=df[y].sum()
  st.bar_chart(df)
