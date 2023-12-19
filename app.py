import streamlit as st

st.title("GemInsights")
file = st.file_uploader("Pick a dataframe", type=["csv"])
text_input = st.text_input(
        "Enter some text 👇",
        label_visibility="visible",
        disabled=False,
        placeholder="enter something", 
    )

if st.button("Get Insights", type="primary"):
    st.write("here are the predictions")
else:
    st.write("")
