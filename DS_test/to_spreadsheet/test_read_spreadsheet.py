import gspread as gs
import pandas as pd
from IPython.display import display

gc = gs.service_account(filename='C:/Users/P5CD1/OneDrive/Documents/GitHub/DataScience_Discuss/DS_test/to_spreadsheet/Gdrive_datascience-upmkr-01-97fd95dae19b.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1SafUj_gvbqx3JAAcmTlHbG-kj19pe2_ElvpP9SRQjMo/edit?usp=sharing')

ws = sh.worksheet('Sheet1')
df = pd.DataFrame(ws.get_all_records())
display(df)