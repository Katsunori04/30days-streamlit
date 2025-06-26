import streamlit as st

# streamlitで日本語
st.set_page_config(
    page_title="Day 12 - st.checkbox",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("30DaysOfStreamlit - Day 12")

st.header("Day 12")
st.write("What would you like to order?")

icecream = st.checkbox("Ice cream")
coffee = st.checkbox("Coffee")
cola = st.checkbox("Cola")

if icecream:
    st.write("Great! Here's some more 🍦")

if coffee:
    st.write("Okay! Here's some coffee ☕")

if cola:
    st.write("Here you go🥤")
