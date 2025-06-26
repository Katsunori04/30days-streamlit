import numpy as np
import pandas as pd
import streamlit as st

# streamlitで日本語
st.set_page_config(
    page_title="Day 9 - st.line_chart",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("30DaysOfStreamlit - Day 9")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"],
)

st.header("Day 9")
st.write("st.line_chart")
st.line_chart(chart_data)
