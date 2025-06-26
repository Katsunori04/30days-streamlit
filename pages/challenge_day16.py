import streamlit as st

# streamlitで日本語
st.set_page_config(
    page_title="Day 16 - Theme Configuration",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("30DaysOfStreamlit - Day 16")

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
