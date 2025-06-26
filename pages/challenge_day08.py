import streamlit as st
from datetime import time, datetime

# streamlitで日本語
st.set_page_config(
    page_title="Day 8 - st.slider",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("30DaysOfStreamlit - Day 8")

# day 8
st.header("Day 8")
st.write("st.slider")

# 例1
st.subheader("st.slider")

age = st.slider("Select your age", 0, 130, 25)
st.write("Your age is", age)

# 例2
st.subheader("Range slider")
values = st.slider("Select a range of values", 0, 100, (25, 75))
st.write("Values:", values)

# 例3
st.subheader("Range time slider")

appointment = st.slider("Schedule your appointment", value=(time(11, 30), time(12, 45)))
st.write("Your appointment is scheduled for", appointment)

# 例4
st.subheader("Datetime slider")
start_time = st.slider(
    "When do you start your day?",
    value=(datetime(2020, 1, 1, 9, 30), datetime(2020, 1, 1, 17, 30)),
    format="MM/DD/YY - hh:mm",
)
st.write("Start time:", start_time)
