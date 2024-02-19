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

try:
    # Get the spreadsheet ID from the URL
    spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1iia808sqxPv4Cfy0SP69foD-sRDqYAys24BdaskU2y4/edit#gid=1680754323'
    spreadsheet_id = spreadsheet_url.split('/')[5]

    # Open the spreadsheet
    SHEET = GSPREAD_CLIENT.open_by_key(spreadsheet_id)

    # Access the "sales" worksheet
    sales = SHEET.worksheet("sales")

    # Get all values from the "sales" worksheet
    data = sales.get_all_values()

    # Print the data
    print(data)

except gspread.exceptions.SpreadsheetNotFound as e:
    print("Could not find spreadsheet. Please check the URL.")


