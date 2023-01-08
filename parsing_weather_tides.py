from bs4 import BeautifulSoup
import time
from selenium import webdriver
import pandas as pd
from pathlib import Path

url = 'https://weather.com/id-ID/weather/tenday/l/Kramat+Daerah+Khusus+Ibukota+Jakarta?canonicalCityId=9d5f83a2a29b1f4aa5272fca53aa871b328c5ee66f6882d07480f0a94b37565c#detailIndex5'
url2 = 'https://www.tideschart.com/Indonesia/Jakarta/Weekly/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
chrome_options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome(chrome_options = chrome_options)
driver2 = webdriver.Chrome(chrome_options = chrome_options)

time.sleep(0.5)
driver.get(url)
driver2.get(url2)
time.sleep(0.5)

soup = BeautifulSoup(driver.page_source, 'lxml')
soup2 = BeautifulSoup(driver2.page_source, 'lxml')

df_01 = list()
for el in soup.find().find_all("summary",{"class" : "Disclosure--Summary--3GiL4 DaypartDetails--Summary--3Fuya Disclosure--hideBorderOnSummaryOpen--3_ZkO"}):
    df_01.append(el.get_text("\n",strip=True).split("\n"))

df_01 = pd.DataFrame(df_01)
df_01 = df_01.drop(df_01.columns[[2, 4, 6, 8, 9,11]], axis=1)
df_01 = df_01.drop(labels = [6,7,8,9,10,11,12,13], axis=0)
#display(df_01)

df_all = []

col_all =[
    "Hari",
    "Temperature_siang_Celcius",
    "Temperature_malam_Celcius",
    "Prediksi_cuaca",
    "Kemungkinan_hujan_persen",
    "Kecepatan_angin_km_per_hour",
    "Waktu_tide_1",
    "Tide_1_meter",
    "Waktu_tide_2",
    "Tide_2_meter"
]
df_all = pd.DataFrame(df_all, columns=col_all)

#display(df_all)

df_02 = list()

for el in soup2.find().find_all("table",{"class" : "table table-hover tidechart mb-4"}):
    fic2 = el.get_text("\n",strip=True)
    #print(fic)
    df_02.append(el.get_text("\n",strip=True).split("\n"))

df_02 = pd.DataFrame(df_02)

df_02_temp = []
df_02_temp = pd.DataFrame(df_02_temp, columns = ["0","1","2","3","4"])
df_02_temp = pd.DataFrame(df_02_temp)

a = 7
b = 8
c = 10
d = 11
e = 13

x = 1
y = 8
while x < y:
    val_col_02 = [
        df_02.iloc[0,a],
        df_02.iloc[0,b],
        df_02.iloc[0,c],
        df_02.iloc[0,d],
        df_02.iloc[0,e],
    ]
    df_02_temp.loc[len(df_02_temp)] = val_col_02
    x += 1
    a += 11
    b += 11
    c += 11
    d += 11
    e += 11
    
df_02 = df_02_temp.drop(labels = 0, axis=0)
df_02.index = range(len(df_02))
#df_02_temp.rename(df_02_temp.iloc[0], axis=0, inplace=True)
#df_02 = df_02_temp.drop(df_02_temp.index[0], axis = 0, inplace=True)
#display(df_02)

df_all["Hari"] = df_01.iloc[:,0]
df_all["Temperature_siang_Celcius"] = df_01.iloc[:,1]
df_all["Temperature_malam_Celcius"] = df_01.iloc[:,2]
df_all["Prediksi_cuaca"] = df_01.iloc[:,3]
df_all["Kemungkinan_hujan_persen"] = df_01.iloc[:,4]
df_all["Kecepatan_angin_km_per_hour"] = df_01.iloc[:,5]

df_all["Waktu_tide_1"] = df_02.iloc[:,1]
df_all["Tide_1_meter"] = df_02.iloc[:,2]
df_all["Waktu_tide_2"] =df_02.iloc[:,3]
df_all["Tide_2_meter"] = df_02.iloc[:,4]
#display(df_all)


df_all['Temperature_siang_Celcius'] = df_all.Temperature_siang_Celcius.str.findall('([-+]?\d*\.?\d+)')
df_all['Temperature_malam_Celcius'] = df_all.Temperature_malam_Celcius.str.findall('([-+]?\d*\.?\d+)')
df_all['Kemungkinan_hujan_persen'] = df_all.Kemungkinan_hujan_persen.str.findall('([-+]?\d*\.?\d+)')
df_all['Kecepatan_angin_km_per_hour'] = df_all.Kecepatan_angin_km_per_hour.str.findall('([-+]?\d*\.?\d+)')
df_all['Tide_1_meter'] = df_all.Tide_1_meter.str.findall('([-+]?\d*\.?\d+)')
df_all['Tide_2_meter'] = df_all.Tide_2_meter.str.findall('([-+]?\d*\.?\d+)')

#df_all.apply(pd.Series.explode)
#df_all.explode()
#display(df_all)
df_all = df_all.apply(pd.Series.explode)
#display(df_all)

my_file = Path("data_weather_tides.csv")
if my_file.is_file():
    df_csv_01 = pd.read_csv("data_weather_tides.csv")
    #df_csv_01 = pd.concat([df_csv_01, df_all])
    df_csv_01.merge(df_all, how='outer', on='Hari')
    df_csv_01.to_csv("data_weather_tides.csv", index = False)
else :
    df_all.to_csv("data_weather_tides.csv", index = False)

driver.quit()