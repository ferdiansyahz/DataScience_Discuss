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

display(df_01)

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
    df_01.iloc[0,7],#beban PLTU 4

    df_01.iloc[0,10],#beban PLTU 5
    df_01.iloc[0,8],#MVAR PLTU 4
    df_01.iloc[0,11],#MVAR PLTU 5
    df_01.iloc[0,13],# Total Beban PLTU
    df_01.iloc[0,14],# Total MVAR PLTU
    df_01.iloc[0,19], # Beban_GTG1_1",

    df_01.iloc[0,22],#"Beban_GTG1_2",
    df_01.iloc[0,25],#"Beban_GTG1_3",
    df_01.iloc[0,28],#"Beban_STG1_1",
    df_01.iloc[0,20],#"MVAR_GTG1_1",

    df_01.iloc[0,23],#"MVAR_GTG1_2",
    df_01.iloc[0,26],#"MVAR_GTG1_3",
    df_01.iloc[0,29],#"MVAR_STG1_1",
    df_01.iloc[0,31],#"Total_Beban_Blok1",
    df_01.iloc[0,32],#"Total_MVAR_Blok1",

    df_01.iloc[0,37],#"Beban_GTG2_1",
    df_01.iloc[0,40],#"Beban_GTG2_2",
    df_01.iloc[0,43],#"Beban_STG2_1",
    df_01.iloc[0,46],#"Beban_STG2_2",
    df_01.iloc[0,49],#"Beban_STG2_3",
    df_01.iloc[0,38],#"MVAR_GTG2_1",
    df_01.iloc[0,41],#"MVAR_GTG2_2",

    df_01.iloc[0,44],#"MVAR_STG2_1",
    df_01.iloc[0,47],#"MVAR_STG2_2",
    df_01.iloc[0,50],#"MVAR_STG2_3",

    df_01.iloc[0,52],#"Total_Beban_Blok2",
    df_01.iloc[0,53],#"Total_MVAR_Blok2",
    df_01.iloc[0,58],#"Beban_GTG3_1",
    df_01.iloc[0,61],#"Beban_STG3_1",
    df_01.iloc[0,59],#"MVAR_GTG3_1",
    df_01.iloc[0,62],#"MVAR_STG3_1",
    df_01.iloc[0,64],#"Total_Beban_Blok3",
    df_01.iloc[0,65],#"Total_MVAR_Blok3",

    df_01.iloc[0,67],#"Total_Beban_UnitEksisting",
    df_01.iloc[0,68],#"Total_MVAR_UnitEksisting",
    df_01.iloc[0,70],#"Total_Beban_UnitAMC",
    df_01.iloc[0,71],#"Total_MVAR_UnitAMC",
    df_01.iloc[0,73],#"Total_Beban_UPMKR",
    df_01.iloc[0,77],#"Total_MVAR_UPMKR",
    df_01.iloc[0,75]#"Total_Frekuensi_UPMKR"
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

