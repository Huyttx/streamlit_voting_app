import streamlit as st
from pages.auth import check_user
from pages.vote import voting_page
from pages.admin import admin_page

st.set_page_config(page_title="Ứng dụng bầu cử", layout="centered")
st.title("🗳️ Ứng dụng bầu chọn")

page = st.sidebar.selectbox("Chọn chức năng", ["Bầu cử", "Quản trị"])
user_id = st.sidebar.text_input("Nhập mã bầu cử:", key="user_input")

if user_id:
    if page == "Bầu cử":
        if check_user(user_id):
            voting_page(user_id)
        else:
            st.error("❌ Mã người dùng không hợp lệ.")
    elif page == "Quản trị":
        admin_page(user_id)