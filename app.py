import streamlit as st
import pandas as pd
import os
from gemInsights.utils.common import save_json, load_json
from pathlib import Path
from gemInsights import logger
from markdown import markdown


if not os.path.isdir("streamlit_files"):
    os.makedirs(os.path.join(os.getcwd(), "streamlit_files"), exist_ok=True)

dataframe = None
st.title("GemInsights")
file = st.file_uploader(
    "Pick a dataframe", type=["csv", "xlsx"], accept_multiple_files=False
)

if file is not None:
    _, extension = os.path.splitext(file.name)
    if extension == ".csv":
        dataframe = pd.read_csv(file)
    else:
        dataframe = pd.read_excel(file)
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
        placeholder="Select one column in here",
    )

if st.button("Get Insights", type="primary"):
    dataframe.to_csv("streamlit_files/data.csv")
    logger.info(f"saved the data at streamlit_files/data.csv")

    additional_info = {"additional_info": text_input, "target_col": option}
    save_json(path="streamlit_files/additional_data.json", data=additional_info)

    st.write("generating insights ...")
    # running the pipeline
    os.system("python main.py")

    response = load_json(Path("artifacts/prompting/response.json"))
    res = markdown(response.response)
    st.markdown(res, unsafe_allow_html=True)

else:
    st.write("")
