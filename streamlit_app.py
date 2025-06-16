import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.title("30DaysOfStreamlit")

# day 2
st.header("Day 2")
st.write("Hello world!")

# day 3
st.header("Day 3")
st.header("st.button")

if st.button("Say hello"):
    st.write("Why hello there!")
else:
    st.write("Goodbye")

# day 4
st.header("Day 4")
st.write("動画を見た")

# day 5
st.header("Day 5")
st.write("st.write")

# 例1
st.write("Hello, *World!* :sunglasses:")

# 例2
st.write(1234)

# 例3
df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
st.write(df)

# 例4
st.write("Below is a DataFrame:", df, "Above is a dataframe")

# 例5
df2 = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
c = (
    alt.Chart(df2)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)
st.write(c)

# day 6
st.header("Day 6")
st.write("Githubにアップロードした")

# day 7
st.header("Day 7")
st.write("streamlit cloudにアップロードした")

# day 8
from datetime import time, datetime

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
