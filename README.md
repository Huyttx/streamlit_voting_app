# Streamlit Voting App with Google Sheets

## Cấu trúc
- Sử dụng Google Sheets cho:
  - Danh sách ứng viên (`candidates`)
  - Số phiếu bầu (`votes`)
  - Người đã bầu (`voted_users`)
  - Danh sách được phép bầu (`allowed_users`)

## Cách chạy
1. Tạo Google Sheet có các tab trên.
2. Chia sẻ quyền `Editor` cho service account.
3. Đặt file `credentials.json` vào thư mục gốc.
4. `pip install streamlit gspread pandas`
5. `streamlit run main.py`