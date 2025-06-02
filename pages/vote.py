import streamlit as st
from pages.utils import get_candidates, record_vote, has_voted

def voting_page(user_id):
    if has_voted(user_id):
        st.warning("⚠️ Bạn đã bầu rồi.")
        return

    candidates = get_candidates()
    st.markdown("### Danh sách ứng viên")
    for c in candidates:
        st.markdown(f"- **{c['name']}** ({c['position']}, {c['birth_year']})")

    selection = st.multiselect("✅ Chọn ứng viên:", [c["name"] for c in candidates])
    if st.button("📝 Gửi phiếu bầu"):
        if 1 <= len(selection) <= 3:
            record_vote(user_id, selection)
            st.success("Phiếu bầu đã được ghi nhận.")
        else:
            st.error("Chọn ít nhất 1 và tối đa 3 ứng viên.")