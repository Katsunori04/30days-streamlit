import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

# streamlitで日本語
st.set_page_config(
    page_title="Day 5 - st.write",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("30DaysOfStreamlit - Day 5")

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
