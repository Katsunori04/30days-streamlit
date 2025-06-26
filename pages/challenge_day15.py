import streamlit as st

# streamlitで日本語
st.set_page_config(
    page_title="Day 15 - st.latex",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("30DaysOfStreamlit - Day 15")

# day 15
st.header("Day 15")
st.subheader("st.latex")
st.latex(
    r"""
    a^2 + b^2 = c^2
"""
)
