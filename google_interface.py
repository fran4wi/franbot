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
        
    
    def LOG_ERROR(self, row: list):
        self._check_for_service_account(f"{__file__}:ERRORS()");
        try: 
            sheet : gspread.Worksheet = self.sheets["ERRORS"]
            row.insert(0, datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            sheet.append_row(row)
            
        except KeyError:
            raise Exception(f"ERRORS google sheet does not seem to exist! {__file__}:ERRORS()")
    def fran(self, row: list = []):
        self._check_for_service_account(f"{__file__}:fran()");
        try: 
            sheet : gspread.Worksheet = self.sheets["FRAN_COMMAND"]
            row.insert(0, datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            sheet.append_row(row)
            
        except KeyError:
            raise Exception(f"ERRORS google sheet does not seem to exist! {__file__}:FRAN_COMMAND()")
        
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
            sheet.append_row([ datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),id, profile_email, first_name, last_name, event_ts])
            
        except KeyError:
            raise Exception(f"ERRORS google sheet does not seem to exist! {__file__}:ERRORS()")
    
    
        # self.sheets
        
        
        
container = Google_Container()