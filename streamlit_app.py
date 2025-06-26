# streamlit 30days - stremlit_app.py
# top page for the 30 Days of Streamlit challenge
import streamlit as st

# streamlitで日本語
st.set_page_config(
    page_title="30DaysOfStreamlit",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("30 Days of Streamlit")

st.markdown(
    """
    30 Days of Streamlitのまとめページです。  
    サイドバーのマルチリンクから、詳細な内容を確認できます。
    """
)
