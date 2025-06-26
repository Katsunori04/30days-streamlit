import streamlit as st

# streamlitで日本語
st.set_page_config(
    page_title="Day 17 - st.secrets",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("30DaysOfStreamlit - Day 17")

# day17
st.header("Day 17")
st.subheader("st.secrets")

st.write(st.secrets["message"])
