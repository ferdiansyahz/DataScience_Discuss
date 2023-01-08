from bs4 import BeautifulSoup
import time
from selenium import webdriver
import pandas as pd
from pathlib import Path

url = 'https://bpbd.jakarta.go.id/waterlevel'


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

#TANGGAL
for el in soup.find().find_all("div",{"class" : "newsbox__cate"}):
    fic = el.get_text("\n",strip=True)
    #print(fic)
    #df_01.append(el.get_text("\n",strip=True).split("\n"))

#JAM
df_01 = list()
for el in soup.find().find_all("thead"):
    fic2 = el.get_text("\n",strip=True)
    #print(fic2)
    df_01.append(el.get_text("\n",strip=True).split("\n"))

df_01 = pd.DataFrame(df_01)
#display(df_01)

df_01 = df_01.drop(df_01.columns[[0,1]], axis = 1)
df_01 = df_01.T
#df_01 = df_01.sort_values(by = [0])
df_01.index = range(len(df_01))
#df_01 = fic + "," + " " + df_01.astype(str)
#df_01 = df_01.rename({0 : 'Tanggal'}, axis = 1)
#display(df_01)

#VALUE
df_02 = list()
for el in soup.find().find_all("tbody"):
    fic3 = el.get_text("\n",strip=True)
    #print(fic3)
    df_02.append(el.get_text("\n",strip=True).split("\n"))

df_02 = pd.DataFrame(df_02)
df_02 = df_02.T
#display(df_02)

df_all = df_01
#display(df_all)

#Bendungan Katulampa
df_02 = df_02.rename({0 : 'dummy'}, axis = 1)
idx_start = df_02.index[df_02.dummy == "Bendung Katulampa"]

idx_end = df_02.index[df_02.dummy== "Pos Depok"]
subset_df = []
for i_start, i_end in zip(idx_start, idx_end):
    subset_df.append(df_02.iloc[(i_start+1):i_end, :])

merged_df = pd.concat(subset_df)
#merged_df = merged_df.sort_values(by = ['dummy'])
merged_df.index = range(len(merged_df))
df_all['Bendungan_Katulampa'] = merged_df['dummy']

#Pos Depok
idx_start = df_02.index[df_02.dummy == "Pos Depok"]
idx_end = df_02.index[df_02.dummy== "Manggarai BKB"]

subset_df = []
for i_start, i_end in zip(idx_start, idx_end):
    subset_df.append(df_02.iloc[(i_start+1):i_end, :])

merged_df = pd.concat(subset_df)
#merged_df = merged_df.sort_values(by = ['dummy'])
merged_df.index = range(len(merged_df))
df_all['Pos_Depok'] = merged_df['dummy']

#Manggarai BKB
idx_start = df_02.index[df_02.dummy == "Manggarai BKB"]
idx_end = df_02.index[df_02.dummy== "PA. Karet"]

subset_df = []
for i_start, i_end in zip(idx_start, idx_end):
    subset_df.append(df_02.iloc[(i_start+1):i_end, :])

merged_df = pd.concat(subset_df)
#merged_df = merged_df.sort_values(by = ['dummy'])
merged_df.index = range(len(merged_df))
df_all['Manggarai_BKB'] = merged_df['dummy']

#PA. Karet
idx_start = df_02.index[df_02.dummy == "PA. Karet"]
idx_end = df_02.index[df_02.dummy== "Pos Krukut Hulu"]

subset_df = []
for i_start, i_end in zip(idx_start, idx_end):
    subset_df.append(df_02.iloc[(i_start+1):i_end, :])

merged_df = pd.concat(subset_df)
#merged_df = merged_df.sort_values(by = ['dummy'])
merged_df.index = range(len(merged_df))
df_all['PA_Karet'] = merged_df['dummy']

#Pos Krukut Hulu
idx_start = df_02.index[df_02.dummy == "Pos Krukut Hulu"]
idx_end = df_02.index[df_02.dummy== "Pos Pesanggrahan"]

subset_df = []
for i_start, i_end in zip(idx_start, idx_end):
    subset_df.append(df_02.iloc[(i_start+1):i_end, :])

merged_df = pd.concat(subset_df)
#merged_df = merged_df.sort_values(by = ['dummy'])
merged_df.index = range(len(merged_df))
df_all['Pos_Krukut_Hulu'] = merged_df['dummy']

#Pos Pesanggrahan
idx_start = df_02.index[df_02.dummy == "Pos Pesanggrahan"]
idx_end = df_02.index[df_02.dummy== "Pos Angke Hulu"]

subset_df = []
for i_start, i_end in zip(idx_start, idx_end):
    subset_df.append(df_02.iloc[(i_start+1):i_end, :])

merged_df = pd.concat(subset_df)
#merged_df = merged_df.sort_values(by = ['dummy'])
merged_df.index = range(len(merged_df))
df_all['Pos_Pesanggrahan'] = merged_df['dummy']

#Pos Angke Hulu
idx_start = df_02.index[df_02.dummy == "Pos Angke Hulu"]
idx_end = df_02.index[df_02.dummy== "Waduk Pluit"]

subset_df = []
for i_start, i_end in zip(idx_start, idx_end):
    subset_df.append(df_02.iloc[(i_start+1):i_end, :])

merged_df = pd.concat(subset_df)
#merged_df = merged_df.sort_values(by = ['dummy'])
merged_df.index = range(len(merged_df))
df_all['Pos_Angke_Hulu'] = merged_df['dummy']

#Pos Waduk Pluit
idx_start = df_02.index[df_02.dummy == "Waduk Pluit"]
idx_end = df_02.index[df_02.dummy== "Pasar Ikan - Laut"]

subset_df = []
for i_start, i_end in zip(idx_start, idx_end):
    subset_df.append(df_02.iloc[(i_start+1):i_end, :])

merged_df = pd.concat(subset_df)
#merged_df = merged_df.sort_values(by = ['dummy'])
merged_df.index = range(len(merged_df))
df_all['Waduk_Pluit'] = merged_df['dummy']

#Pasar Ikan - Laut
idx_start = df_02.index[df_02.dummy == "Pasar Ikan - Laut"]
idx_end = df_02.index[df_02.dummy== "Pos Cipinang Hulu"]

subset_df = []
for i_start, i_end in zip(idx_start, idx_end):
    subset_df.append(df_02.iloc[(i_start+1):i_end, :])

merged_df = pd.concat(subset_df)
#merged_df = merged_df.sort_values(by = ['dummy'])
merged_df.index = range(len(merged_df))
df_all['Pasar_Ikan_Laut'] = merged_df['dummy']

#Pos Cipinang Hulu
idx_start = df_02.index[df_02.dummy == "Pos Cipinang Hulu"]
idx_end = df_02.index[df_02.dummy== "Pos Sunter Hulu"]

subset_df = []
for i_start, i_end in zip(idx_start, idx_end):
    subset_df.append(df_02.iloc[(i_start+1):i_end, :])

merged_df = pd.concat(subset_df)
#merged_df = merged_df.sort_values(by = ['dummy'])
merged_df.index = range(len(merged_df))
df_all['Pos_Cipinang_Hulu'] = merged_df['dummy']

#Pos Sunter Hulu
idx_start = df_02.index[df_02.dummy == "Pos Sunter Hulu"]
idx_end = df_02.index[df_02.dummy== "Pulo Gadung"]

subset_df = []
for i_start, i_end in zip(idx_start, idx_end):
    subset_df.append(df_02.iloc[(i_start+1):i_end, :])

merged_df = pd.concat(subset_df)
#merged_df = merged_df.sort_values(by = ['dummy'])
merged_df.index = range(len(merged_df))
df_all['Pos_Sunter_Hulu'] = merged_df['dummy']

#Pulo Gadung
df_02.loc[len(df_02.index)] = ['Final']
idx_start = df_02.index[df_02.dummy == "Pulo Gadung"]
idx_end = df_02.index[df_02.dummy== "Final"]

subset_df = []
for i_start, i_end in zip(idx_start, idx_end):
    subset_df.append(df_02.iloc[(i_start+1):i_end, :])

merged_df = pd.concat(subset_df)
#merged_df = merged_df.sort_values(by = ['dummy'])
merged_df.index = range(len(merged_df))
df_all['Pulo_Gadung'] = merged_df['dummy']

#display(df_all)

df_all = df_all.sort_values(by = [0])
df_all.index = range(len(df_all))
df_all = df_all.rename({0 : 'Tanggal'}, axis = 1)
df_all['Tanggal'] = fic + "," + " " + df_all['Tanggal'].astype(str)

df_all['Bendungan_Katulampa'] = df_all.Bendungan_Katulampa.str.findall('([-+]?\d*\.?\d+)')
df_all['Pos_Depok'] = df_all.Pos_Depok.str.findall('([-+]?\d*\.?\d+)')
df_all['Manggarai_BKB'] = df_all.Manggarai_BKB.str.findall('([-+]?\d*\.?\d+)')
df_all['PA_Karet'] = df_all.PA_Karet.str.findall('([-+]?\d*\.?\d+)')
df_all['Pos_Krukut_Hulu'] = df_all.Pos_Krukut_Hulu.str.findall('([-+]?\d*\.?\d+)')
df_all['Pos_Pesanggrahan'] = df_all.Pos_Pesanggrahan.str.findall('([-+]?\d*\.?\d+)')
df_all['Pos_Angke_Hulu'] = df_all.Pos_Angke_Hulu.str.findall('([-+]?\d*\.?\d+)')
df_all['Waduk_Pluit'] = df_all.Waduk_Pluit.str.findall('([-+]?\d*\.?\d+)')
df_all['Pasar_Ikan_Laut'] = df_all.Pasar_Ikan_Laut.str.findall('([-+]?\d*\.?\d+)')
df_all['Pos_Cipinang_Hulu'] = df_all.Pos_Cipinang_Hulu.str.findall('([-+]?\d*\.?\d+)')
df_all['Pos_Sunter_Hulu'] = df_all.Pos_Sunter_Hulu.str.findall('([-+]?\d*\.?\d+)')
df_all['Pulo_Gadung'] = df_all.Pulo_Gadung.str.findall('([-+]?\d*\.?\d+)')

df_all = df_all.apply(pd.Series.explode)

#display(df_all)

my_file = Path("data_water_level.csv")
if my_file.is_file():
    df_csv_01 = pd.read_csv("data_water_level.csv")
    #df_csv_01 = pd.concat([df_csv_01, df_all])
    df_csv_01.merge(df_all, how='outer', on='Tanggal')
    df_csv_01.to_csv("data_water_level.csv", index = False)
else :
    df_all.to_csv("data_water_level.csv", index = False)

driver.quit()