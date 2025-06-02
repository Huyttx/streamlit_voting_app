import gspread

def get_worksheet(sheet_name, worksheet_name):
    gc = gspread.service_account(filename="credentials.json")
    sh = gc.open(sheet_name)
    return sh.worksheet(worksheet_name)

def check_user(user_id):
    ws = get_worksheet("ElectionData", "allowed_users")
    users = ws.col_values(1)
    return user_id in users