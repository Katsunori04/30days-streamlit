Simport streamlit as st


st.title("st.form")

# with表記の使用例
# ※「完全な」は「Full」の訳だと思いますが訳さなくても伝わると思います。
st.header("1. Example of using `with` notation")
st.subheader("Coffee machine")

with st.form("my_form"):
    st.subheader("** Order your coffe **")

    # 入力ウィジェット
    coffee_bean_val = st.selectbox("Coffee bean", ["Arabica", "Robusta"])
    coffee_roast_val = st.selectbox("Coffee roast", ["Light", "Medium", "Dark"])
    brewing_val = st.selectbox(
        "Brewing method", ["Aeropress", "Drip", "French press", "Moka pot", "Siphon"]
    )
    serving_type_val = st.selectbox("Serving format", ["Hot", "Iced", "Frappe"])
    milk_val = st.select_slider("Milk intensity", ["None", "Low", "Medium", "High"])
    owncup_val = st.checkbox("Bring own cup")

    # すべてのフォームには送信ボタンが必要です
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.markdown(
            f"""
            ? Your order
            - Coffee bean: {coffee_bean_val}
            - Coffee roast: {coffee_roast_val}
            - Brewing method: {brewing_val}
            - Serving format: {serving_type_val}
            - Milk intensity: {milk_val}
            - Bring own cup: {owncup_val}
            """
        )
    else:
        st.markdown("Please fill out the form and click the submit button.")
