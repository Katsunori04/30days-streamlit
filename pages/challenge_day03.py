import streamlit as st

# streamlitで日本語
st.set_page_config(
    page_title="Day 3 - Button",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("30DaysOfStreamlit - Day 3")

# day 3
st.header("Day 3")
st.header("st.button")

if st.button("Say hello"):
    st.write("Why hello there!")
else:
    st.write("Goodbye")
