import requests
from bs4 import BeautifulSoup
import pandas as pd
import pandas as pd
from IPython.display import display

#------Pakai proxy kantor
url = "http://192.168.17.65/kinerja-operasi/public/telemetri"
r = requests.get(url,verify=False)
soup = BeautifulSoup(r.content, "lxml")

#------Testing pakai saving html
#url = "C:/Users/P5CD1/OneDrive/Documents/GitHub/DataScience_Discuss/DS_test/Scrapping_telemetriBebanUPMKR/web_telemetriUPMKR.html"
#page = open(url)
#soup = BeautifulSoup(page.read())


df_01 = list()
for el in soup.find_all("div",{"class" : "container-fluid"}):
    df_01.append(el.get_text("\n",strip=True).split("\n"))

df_01 = pd.DataFrame(df_01)

df_02 = []
col_02 = [
    "Tanggal",
    "Beban_PLTU4",
    "Beban_PLTU5",
    "MVAR_PLTU4",
    "MVAR_PLTU5",
    "Total_Beban_PLTU",
    "Total_MVAR_PLTU",
    "Beban_GTG1_1",
    "Beban_GTG1_2",
    "Beban_GTG1_3",
    "Beban_STG1_1",
    "MVAR_GTG1_1",
    "MVAR_GTG1_2",
    "MVAR_GTG1_3",
    "MVAR_STG1_1",
    "Total_Beban_Blok1",
    "Total_MVAR_Blok1",
    "Beban_GTG2_1",
    "Beban_GTG2_2",
    "Beban_STG2_1",
    "Beban_STG2_2",
    "Beban_STG2_3",
    "MVAR_GTG2_1",
    "MVAR_GTG2_2",
    "MVAR_STG2_1",
    "MVAR_STG2_2",
    "MVAR_STG2_3",
    "Total_Beban_Blok2",
    "Total_MVAR_Blok2",
    "Beban_GTG3_1",
    "Beban_STG3_1",
    "MVAR_GTG3_1",
    "MVAR_STG3_1",
    "Total_Beban_Blok3",
    "Total_MVAR_Blok3",
    "Total_Beban_UnitEksisting",
    "Total_MVAR_UnitEksisting",
    "Total_Beban_UnitAMC",
    "Total_MVAR_UnitAMC",
    "Total_Beban_UPMKR",
    "Total_MVAR_UPMKR",
    "Total_Frekuensi_UPMKR"
    ]
df_02 = pd.DataFrame(df_02, columns=col_02)

val_col_02 =[
    df_01.iloc[0,2],#tanggal
    df_01.iloc[1,4],#beban PLTU 4
    df_01.iloc[1,7],#beban PLTU 5
    df_01.iloc[1,5],#MVAR PLTU 4
    df_01.iloc[1,8],#MVAR PLTU 5
    df_01.iloc[1,10],# Total Beban PLTU
    df_01.iloc[1,11],# Total MVAR PLTU
    df_01.iloc[1,16], # Beban_GTG1_1",
    df_01.iloc[1,19],#"Beban_GTG1_2",
    df_01.iloc[1,22],#"Beban_GTG1_3",
    df_01.iloc[1,25],#"Beban_STG1_1",
    df_01.iloc[1,17],#"MVAR_GTG1_1",
    df_01.iloc[1,20],#"MVAR_GTG1_2",
    df_01.iloc[1,23],#"MVAR_GTG1_3",
    df_01.iloc[1,26],#"MVAR_STG1_1",
    df_01.iloc[1,28],#"Total_Beban_Blok1",
    df_01.iloc[1,29],#"Total_MVAR_Blok1",
    df_01.iloc[1,34],#"Beban_GTG2_1",
    df_01.iloc[1,37],#"Beban_GTG2_2",
    df_01.iloc[1,40],#"Beban_STG2_1",
    df_01.iloc[1,43],#"Beban_STG2_2",
    df_01.iloc[1,46],#"Beban_STG2_3",
    df_01.iloc[1,35],#"MVAR_GTG2_1",
    df_01.iloc[1,38],#"MVAR_GTG2_2",
    df_01.iloc[1,41],#"MVAR_STG2_1",
    df_01.iloc[1,44],#"MVAR_STG2_2",
    df_01.iloc[1,47],#"MVAR_STG2_3",
    df_01.iloc[1,49],#"Total_Beban_Blok2",
    df_01.iloc[1,50],#"Total_MVAR_Blok2",
    df_01.iloc[1,55],#"Beban_GTG3_1",
    df_01.iloc[1,58],#"Beban_STG3_1",
    df_01.iloc[1,56],#"MVAR_GTG3_1",
    df_01.iloc[1,59],#"MVAR_STG3_1",
    df_01.iloc[1,61],#"Total_Beban_Blok3",
    df_01.iloc[1,62],#"Total_MVAR_Blok3",
    df_01.iloc[1,64],#"Total_Beban_UnitEksisting",
    df_01.iloc[1,65],#"Total_MVAR_UnitEksisting",
    df_01.iloc[1,67],#"Total_Beban_UnitAMC",
    df_01.iloc[1,68],#"Total_MVAR_UnitAMC",
    df_01.iloc[1,70],#"Total_Beban_UPMKR",
    df_01.iloc[1,74],#"Total_MVAR_UPMKR",
    df_01.iloc[1,72]#"Total_Frekuensi_UPMKR"
]

df_02.loc[len(df_02)] = val_col_02

df_02['Total_Beban_Blok3'] = df_02.Total_Beban_Blok3.str.findall('([-+]?\d*\.?\d+)')
df_02['Total_MVAR_Blok3'] = df_02.Total_MVAR_Blok3.str.findall('([-+]?\d*\.?\d+)')

df_02['Total_Beban_UnitEksisting'] = df_02.Total_Beban_UnitEksisting.str.findall('([-+]?\d*\.?\d+)')
df_02['Total_MVAR_UnitEksisting'] = df_02.Total_MVAR_UnitEksisting.str.findall('([-+]?\d*\.?\d+)')

df_02['Total_Beban_UnitAMC'] = df_02.Total_Beban_UnitAMC.str.findall('([-+]?\d*\.?\d+)')
df_02['Total_MVAR_UnitAMC'] = df_02.Total_MVAR_UnitAMC.str.findall('([-+]?\d*\.?\d+)')

df_02['Total_Beban_UPMKR'] = df_02.Total_Beban_UPMKR.str.findall('([-+]?\d*\.?\d+)')
df_02['Total_MVAR_UPMKR'] = df_02.Total_MVAR_UPMKR.str.findall('([-+]?\d*\.?\d+)')
df_02['Total_Frekuensi_UPMKR'] = df_02.Total_Frekuensi_UPMKR.str.findall('([-+]?\d*\.?\d+)')

df_02 = df_02.apply(pd.Series.explode)
cols_numeric = df_02.columns.drop('Tanggal')
df_02[cols_numeric] = df_02[cols_numeric].apply(pd.to_numeric, errors='coerce')

import datetime
df_02.insert(0, 'Datetime', df_02.index + 1)
df_02['Datetime'] = datetime.datetime.now()

display(df_02)

from pathlib import Path
my_file = Path("telemetri_upmkr.csv")
if my_file.is_file():
    df_csv_01 = pd.read_csv("telemetri_upmkr.csv")

    result = pd.concat([df_csv_01, df_02]).drop_duplicates(subset=["Datetime"], keep="last")
    
    result.to_csv("telemetri_upmkr.csv", index = False)
else :
    df_02.to_csv("telemetri_upmkr.csv", index = False)



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

hostname="localhost"
dbname="ews"
uname="root"
pwd="Adminkonin4"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))

session = sessionmaker(bind=engine)()
                               

df_02.to_sql('telemetri_current', engine, if_exists='replace', index=False)
df_02.to_sql('telemetri_hystoriant', engine, if_exists='append', index=False)


engine.dispose()
session.close()

