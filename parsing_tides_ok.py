from bs4 import BeautifulSoup
import time
from selenium import webdriver
import pandas as pd
from pathlib import Path
from IPython.display import display
from sqlalchemy import create_engine
import datetime
import re
import json
import numpy as np

url = 'https://www.tideschart.com/Indonesia/Jakarta/Weekly/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
chrome_options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome(chrome_options = chrome_options)

time.sleep(0.5)
driver.get(url)
time.sleep(0.5)

soup = BeautifulSoup(driver.page_source, 'lxml')

fic = soup.select_one("script:contains('data1')")
fic = fic.get_text("{", strip = True)
#print(fic)
fic = fic[fic.find('{date:'):]
sep = '],'
fic = fic.split(sep, 1)[0]
#print(fic)

#pattern = r'"([A-Za-z0-9_\./\\-]*)"'
pattern_tanggal_waktu = r'"(.*?)"'
tanggal_waktu_raw = re.findall(pattern_tanggal_waktu, fic)
#print(tanggal_waktu_raw)

#pattern_value_tide = r"[-+]?(?:\d*\.*\d+)"
pattern_value_tide = r'(?<=value\:\s)(?:\d*\.*\d+)'
value_tide_raw = re.findall(pattern_value_tide, fic)
#print(value_tide_raw)
#fic = list(fic)

df_01 = pd.DataFrame(tanggal_waktu_raw)
df_01 = df_01.tail(df_01.shape[0]-2)
df_01 = df_01.head(df_01.shape[0]-2)
df_01.index = range(len(df_01))
#display(df_01)

df_02 = pd.DataFrame(value_tide_raw)
df_02 = df_02.tail(df_02.shape[0]-1)
df_02 = df_02.head(df_02.shape[0]-1)
df_02.index = range(len(df_02))
#display(df_02)

df_01['tanggal'] = ''
#display(df_01)

i = 0
j = 0
k = 1

while i <= 13:
    df_01.loc[i, 'tanggal'] = df_01.iloc[j,0] + ' ' + df_01.iloc[k,0]
    i += 1
    j += 2
    k += 2

df_01 = df_01.drop(df_01.columns[[0]], axis=1)
df_01 = df_01.drop(labels = [14,15,16,17,18,19,20,21,22,23,24,25,26,27], axis = 0)
df_01.index = range(len(df_01))
#display(df_01)

df_01['tanggal'] = pd.to_datetime(df_01['tanggal'])

df_02 = df_02.rename(columns={0: 'Value_tide'})

df_01['Datetime_tide1'] = ''
df_01['Datetime_tide2'] = ''

x = 0
y = 0
z = 1
while x <= 6:
    df_01.loc[x, 'Datetime_tide1'] = df_01.iloc[y,0]
    df_01.loc[x, 'Datetime_tide2'] = df_01.iloc[z,0]
    x += 1
    y += 2
    z += 2

df_01 = df_01.drop(df_01.columns[[0]], axis=1)
df_01 = df_01.drop(labels = [7,8,9,10,11,12,13], axis = 0)
df_01.index = range(len(df_01))

df_02['tide1'] = ''
df_02['tide2'] = ''

x = 0
y = 0
z = 1
while x <= 6:
    df_02.loc[x, 'tide1'] = df_02.iloc[y,0]
    df_02.loc[x, 'tide2'] = df_02.iloc[z,0]
    x += 1
    y += 2
    z += 2

df_02 = df_02.drop(df_02.columns[[0]], axis=1)
df_02 = df_02.drop(labels = [7,8,9,10,11,12,13], axis = 0)
df_02.index = range(len(df_02))

#display(df_02)
#display(df_01)

df_all = []
df_all = pd.DataFrame(df_all, columns =[
    "Datetime_taken",
    "Datetime_tide1",
    "tide1",
    "Datetime_tide2",
    "tide2"
]
)


df_all['Datetime_tide1'] = df_01['Datetime_tide1']
df_all['tide1'] = df_02['tide1']
df_all['Datetime_tide2'] = df_01['Datetime_tide2']
df_all['tide2'] = df_02['tide2']

df_all.tide1 = pd.to_numeric(df_all.tide1, errors='coerce')
df_all.tide2 = pd.to_numeric(df_all.tide2, errors='coerce')

df_all['Datetime_taken'] = datetime.datetime.now()

#display(df_all)

df_all_1 = df_all.drop(labels = [1,2,3,4,5,6], axis = 0)
df_all_1.index = range(len(df_all_1))
#display(df_all_1)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

hostname="localhost"
dbname="workshop"
uname="root"
pwd="sanjii123"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))

session = sessionmaker(bind=engine)()
                               
df_all_1.to_sql('table_parsing_tides_coba_current', engine, if_exists='replace', index=False)
df_all_1.to_sql('table_parsing_tides_coba_hystorian', engine, if_exists='append', index=False)
df_all.to_sql('table_parsing_un_tides_coba_current', engine, if_exists='replace', index=False)
df_all.to_sql('table_parsing_un_tides_coba_hystorian', engine, if_exists='append', index=False)


engine.dispose()
session.close()


driver.quit()
