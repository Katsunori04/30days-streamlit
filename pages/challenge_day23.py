import streamlit as st


st.title("st.experimental_get_query_params")

with st.expander("about this app"):
    st.write(
        "`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser."
    )

st.header("1. Instructions")
st.markdown(
    """
In the above URL bar of your internet browser, append the following:
`?name=Jack&surname=Beanstalk`
after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
such that it becomes 
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
"""
)

# 2.st.experimental_get_query_paramsのコンテンツ
st.header("2. Contents of st.experimental_get_query_params")
st.write(st.query_params)


# 3.URLからの情報の取得と表示
st.header("3. Retrieving and displaying information from the URL")
surname = st.query_params["surname"]
firstname = st.query_params["firstname"]
st.write(f"Hello **{firstname} {surname}**, how are you?")
