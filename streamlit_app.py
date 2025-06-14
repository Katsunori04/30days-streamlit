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
