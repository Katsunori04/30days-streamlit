import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit.components.v1 import html

# streamlitで日本語
st.set_page_config(
    page_title="Day 14 - Streamlit Components",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("30DaysOfStreamlit - Day 14")

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
