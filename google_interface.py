import gspread
from datetime import datetime
# class GSheetExtension(gspread.Spreadsheet):
    
class Google_Container:
    service_account = None
    sheets: dict = {}
    def __init__(self):
        pass
    def get_worksheet(self, sheet_info: dict) -> gspread.Worksheet:
        workbook = self.service_account.open_by_key(sheet_info.get("workbook_id"))
        sheet = None
        try: 
            sheet = workbook.worksheet(sheet_info.get("worksheet_name"))
        except gspread.WorksheetNotFound:
            sheet = workbook.add_worksheet(sheet_info.get("worksheet_name"),1000,20)
        return sheet
            

    def initialize(self, credentials_dict: dict, sheet_infos: list):
        """
        initialize _summary_

        Args:
            credentials_dict (dict): _description_
            sheet_ids (dict): {USE_CASE_STRING: {"workbook_id" : str}}
        """
        self.service_account = gspread.service_account_from_dict(credentials_dict)
        for sheet_info in  sheet_infos:
            sheet = self.get_worksheet(sheet_info)
            self.sheets[sheet_info.get("worksheet_name")] = sheet
            
        print(self.sheets)
    
    def _check_for_service_account(self, args):
        if self.service_account == None: 
            raise Exception(f"It looks like our Google Container has not been Initialized!  {args}")
        
    
    def ERRORS(self, row: list):
        self._check_for_service_account(f"{__file__}:ERRORS()");
        try: 
            sheet : gspread.Worksheet = self.sheets["ERRORS"]
            row.insert(0, datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
            sheet.append_row(row)
            
        except KeyError:
            raise Exception(f"ERRORS google sheet does not seem to exist! {__file__}:ERRORS()")
    
    
        # if self.sheets.get("ERRORS") == None: 
    def new_user_join(self, event_data:dict):
        """
        write_to_sheet writes the event data for a new user
        joining the workspace to a google sheet
    
        Args:
            event_data (dict): object with profile information about
            the new user who has joined. To see an example, see
            "event_outputs_examples/user_join_event_example.json"
        """
        self._check_for_service_account(f"{__file__}:new_user_join()");
        user: dict = event_data.get("user")
        id: str = user.get("id")
        profile_email: str = user.get("profile").get("email")
        first_name: str = user.get("profile").get("first_name")
        last_name: str = user.get("profile").get("last_name")
        event_ts: str = event_data.get("event_ts")
        try: 
            sheet : gspread.Worksheet = self.sheets["WORKSPACE_JOIN"]
            sheet.append_row([ datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),id, profile_email, first_name, last_name, event_ts])
            
        except KeyError:
            raise Exception(f"ERRORS google sheet does not seem to exist! {__file__}:ERRORS()")
    
    
        # self.sheets
        
        
        
container = Google_Container()


if __name__ == "__main__":
    from dotenv import load_dotenv
    import json 
    from os import getenv
    load_dotenv()
    gsheet_api_key = json.loads(getenv("GOOGLE_SERVICEKEY_JSON"))
    # sheet_ids = {"WORKSPACE_JOIN": {"workbook_id": "17oGBx0-DBi7pVCQJ00RXxMhmGe4TVMyYrDiK2QxCnxc", "worksheet_name": "WORKSPACE_JOIN"}, "ERRORS": {"workbook_id": "17oGBx0-DBi7pVCQJ00RXxMhmGe4TVMyYrDiK2QxCnxc", "worksheet_name": "ERRORS"}}
    with open("examples/event_outputs/team_join.json") as f:
        js = json.load(f)
        
    sheet_ids = [{"workbook_id": "17oGBx0-DBi7pVCQJ00RXxMhmGe4TVMyYrDiK2QxCnxc", "worksheet_name": "WORKSPACE_JOIN"},{"workbook_id": "17oGBx0-DBi7pVCQJ00RXxMhmGe4TVMyYrDiK2QxCnxc", "worksheet_name": "ERRORS"}]
    container.initialize(gsheet_api_key, sheet_ids)
    # container.ERRORS(["this is a test error!", "wooooo"])
    container.new_user_join(js)