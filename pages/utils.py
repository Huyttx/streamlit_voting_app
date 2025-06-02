import gspread
import pandas as pd
from datetime import datetime

def get_worksheet(sheet_name, worksheet_name):
    gc = gspread.service_account(filename="credentials.json")
    sh = gc.open(sheet_name)
    return sh.worksheet(worksheet_name)

def get_candidates():
    ws = get_worksheet("ElectionData", "candidates")
    data = ws.get_all_records()
    return data

def record_vote(user_id, selection):
    vote_ws = get_worksheet("ElectionData", "votes")
    for name in selection:
        cell = vote_ws.find(name)
        if cell:
            vote_ws.update_cell(cell.row, 2, int(vote_ws.cell(cell.row, 2).value) + 1)

    user_ws = get_worksheet("ElectionData", "voted_users")
    user_ws.append_row([user_id, ", ".join(selection), str(datetime.now())])

def has_voted(user_id):
    ws = get_worksheet("ElectionData", "voted_users")
    users = ws.col_values(1)
    return user_id in users

def get_results():
    ws = get_worksheet("ElectionData", "votes")
    data = ws.get_all_records()
    return pd.DataFrame(data)

def add_candidate(name, position, birth_year):
    ws = get_worksheet("ElectionData", "candidates")
    ws.append_row([name, position, birth_year])
    vote_ws = get_worksheet("ElectionData", "votes")
    vote_ws.append_row([name, 0])