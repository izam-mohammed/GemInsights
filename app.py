import streamlit as st
import pandas as pd

dataframe = None
st.title("GemInsights")
file = st.file_uploader("Pick a dataframe", type=["csv"], accept_multiple_files=False)

if file is not None:
    dataframe = pd.read_csv(file)
    dataframe.to_csv("artifacts/data/data.csv")
    st.write(dataframe.head())
    st.write(f"updated a dataframe with shape {dataframe.shape}")

if file is not None:
    text_input = st.text_input(
        "Enter something about the data 👇",
        label_visibility="visible",
        disabled=False,
        placeholder="eg:- This is a sales dataframe", 
    )

    option = st.selectbox(
    "Which is the target column?",
    tuple(list(dataframe.columns)),
    index=None,
    placeholder="Select contact method...",
    )

if st.button("Get Insights", type="primary"):
    st.write("here are the predictions")
else:
    st.write("")
