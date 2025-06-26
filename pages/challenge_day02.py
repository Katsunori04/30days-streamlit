import streamlit as st

# streamlitで日本語
st.set_page_config(
    page_title="Day 2 - Hello World",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("30DaysOfStreamlit - Day 2")

# day 2
st.header("Day 2")
st.write("Hello world!")
