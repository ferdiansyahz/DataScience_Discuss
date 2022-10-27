import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/P5CD1/OneDrive/Documents/GitHub/DataScience_Discuss/DS_test/to_spreadsheet/Gdrive_datascience-upmkr-01-97fd95dae19b.json', scope)

client = gspread.authorize(creds)

sheet = client.create("rooftop1")
sheet.share('ferdiansyah43@gmail.com', perm_type='user', role='writer')

sheet = client.open("rooftop1").sheet1

df = pd.read_csv('C:/Users/P5CD1/OneDrive/Documents/GitHub/DataScience_Discuss/DS_test/to_spreadsheet/Rooftop 1.csv')
sheet.update([df.columns.values.tolist()] + df.values.tolist())
