import os, json
import gspread
def write_to_sheet(event_data):
    user = event_data.get('user')
    id = user.get('id')
    profile_email =user.get('profile').get("email")
    first_name =user.get('profile').get("first_name")
    last_name =user.get('profile').get("last_name")
    JOIN_WS_SHEET_ID = os.environ.get("JOIN_WS_SHEET_ID")
    gc = gspread.service_account(filename='./sheets_env.json')
    sheet = gc.open_by_key(JOIN_WS_SHEET_ID)
    worksheet = sheet.get_worksheet(0)
    worksheet.append_row([id, profile_email,first_name,last_name])
    
    
def user_join_blocks(user_id):
    # user_id = event["user"]["id"]
    with open("texts/welcome.json") as f:
        welcome_text = f.read()
    print("welcome text === ", welcome_text)
    welcome_text = welcome_text.replace("__USER_ID__", user_id)
    welcome_json = json.loads(welcome_text)
    return welcome_json