import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit.components.v1 import html

# streamlitで日本語
st.set_page_config(
    page_title="30DaysOfStreamlit",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)


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

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"],
)

st.header("Day 9")
st.write("st.line_chart")
st.line_chart(chart_data)

st.header("Day 10")
st.header("st.selectbox")

option = st.selectbox("What is your favorite color?", ["Red", "Green", "Blue"])
st.write("Your favorite color is", option)

st.header("Day 11")
st.header("st.multiselect")

optinos = st.multiselect(
    "What are your favorite colors?",
    ["Green", "Yellow", "Red", "Blue", "Purple"],
    ["Yellow", "Red"],
)

st.write("Your favorite colors are:", optinos)

st.header("Day 12")
st.write("Wthat would you like to order?")

icecream = st.checkbox("Ice cream")
coffee = st.checkbox("Coffee")
cola = st.checkbox("Cola")

if icecream:
    st.write("Great! Here's some more ??")

if coffee:
    st.write("Okay! Here's some coffee ?")

if cola:
    st.write("Here you go??")

# day 14
st.header("Day 14")
st.write("streamlit-components")
st.write("streamlit_pandas_profiling")

st.code(
    r"""
    df = pd.read_csv(
        "https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv"
    )

    # プロファイルレポートを生成
    profile = ProfileReport(df, explorative=True)

    # HTMLとして出力
    profile_html = profile.to_html()

    # Streamlitで表示
    st.header("Pandas Profiling Report")
    html(profile_html, height=1000, scrolling=True)
    """,
    language="python",
)

# day 15
st.header("Day 15")
st.subheader("st.latex")
st.latex(
    r"""
    a^2 + b^2 = c^2
"""
)

# day 16
st.header("Day 16")
st.write("Contents of the `.streamlit/config.toml` file of this app")

st.code(
    """
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
"""
)

number = st.sidebar.slider("Select a number:", 0, 10, 5)
st.write("Selected number from slider widget is:", number)

# day17
st.header("Day 17")
st.subheader("st.secrets")

st.write(st.secrets["message"])
