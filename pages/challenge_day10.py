import streamlit as st

# streamlitで日本語
st.set_page_config(
    page_title="Day 10 - st.selectbox",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("30DaysOfStreamlit - Day 10")

st.header("Day 10")
st.header("st.selectbox")

option = st.selectbox("What is your favorite color?", ["Red", "Green", "Blue"])
st.write("Your favorite color is", option)
