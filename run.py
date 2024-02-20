import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from JSON key file
CREDS = ServiceAccountCredentials.from_json_keyfile_name("creds.json", SCOPE)

# Authorize the client
GSPREAD_CLIENT = gspread.authorize(CREDS)

# Get the spreadsheet ID from the URL
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1iia808sqxPv4Cfy0SP69foD-sRDqYAys24BdaskU2y4/edit#gid=1680754323'
spreadsheet_id = spreadsheet_url.split('/')[5]

# Open the spreadsheet
SHEET = GSPREAD_CLIENT.open_by_key(spreadsheet_id)


def get_sales_data():
        """
        Get sales figures input from the user
        """
        print("Please enter sales data from the last market.")
        print("Data should be be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")
        
        data_str_data = input("Enter your data here:")
        print(f"The data provided is {data_str}")
        
get_sales_data()   
