import streamlit as st
from pages.utils import get_candidates, get_results, add_candidate

ADMIN_PASS = "admin123"

def admin_page(user_id):
    pw = st.text_input("Nhập mật khẩu quản trị", type="password")
    if pw != ADMIN_PASS:
        st.error("Sai mật khẩu.")
        return

    st.header("📊 Quản trị ứng viên")
    candidates = get_candidates()
    st.write("### Danh sách ứng viên hiện tại")
    for c in candidates:
        st.markdown(f"- {c['name']} ({c['position']}, {c['birth_year']})")

    st.write("### ➕ Thêm ứng viên")
    name = st.text_input("Tên")
    position = st.text_input("Chức vụ")
    birth_year = st.number_input("Năm sinh", step=1, min_value=1900)
    if st.button("Thêm mới"):
        if name and position and birth_year:
            add_candidate(name, position, int(birth_year))
            st.success("Đã thêm ứng viên.")
        else:
            st.error("Vui lòng điền đầy đủ thông tin.")

    st.write("### 📈 Kết quả bầu chọn")
    st.dataframe(get_results())