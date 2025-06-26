import streamlit as st

# streamlitで日本語
st.set_page_config(
    page_title="Day 11 - st.multiselect",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("30DaysOfStreamlit - Day 11")

st.header("Day 11")
st.header("st.multiselect")

optinos = st.multiselect(
    "What are your favorite colors?",
    ["Green", "Yellow", "Red", "Blue", "Purple"],
    ["Yellow", "Red"],
)

st.write("Your favorite colors are:", optinos)
