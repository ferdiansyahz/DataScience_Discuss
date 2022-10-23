import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine

url = "https://weather.com/id-ID/weather/tenday/l/Kramat+Daerah+Khusus+Ibukota+Jakarta?canonicalCityId=9d5f83a2a29b1f4aa5272fca53aa871b328c5ee66f6882d07480f0a94b37565c#detailIndex5"

r = requests.get(url,verify=False)
soup = BeautifulSoup(r.content, "lxml")

df = pd.DataFrame(columns = [
'Hari_Tanggal',
'temperature_siang',
'temperatur_malam',
'UV_Index',
'Bulan_Terbenam',
'Bulan_Terbit', 
'Fase_Bulan', 
'Matahari_Terbit',
'Matahari_Terbenam',
'Kecepatan_Angin',
'Humidity',
'Perkiraan_Cuaca'
])
print(df)

n=0
for j in range(n,15):

    hari = "detailIndex"+str(j)

    waktu = soup.find(id=hari).find("h3", {"data-testid": "daypartName", "class": "DetailsSummary--daypartName--2FBp2"})

    temp_data_siang = soup.find(id=hari).find("span", {"data-testid": "TemperatureValue", "class": "DetailsSummary--highTempValue--3Oteu"})
    temp_data_malam = soup.find(id=hari).find("span", {"data-testid": "TemperatureValue", "class": "DetailsSummary--lowTempValue--3H-7I"})
    
    humid = soup.find(id=hari).find("span", {"data-testid": "PercentageValue"})

    uv_index = soup.find(id=hari).find("span", {"data-testid": "UVIndexValue", "class": "DetailsTable--value--1q_qD"})
    bulan_terbenam = soup.find(id=hari).find("span", {"data-testid": "MoonsetTime", "class": "DetailsTable--value--1q_qD"})
    bulan_terbit = soup.find(id=hari).find("span", {"data-testid": "MoonriseTime", "class": "DetailsTable--value--1q_qD"})
    Fase_bulan = soup.find(id=hari).find("span", {"data-testid": "moonPhase", "class": "DetailsTable--moonPhrase--2WlTc"})

    Matahari_terbit = soup.find(id=hari).find("span", {"data-testid": "SunriseTime", "class": "DetailsTable--value--1q_qD"})
    Matahari_terbenam = soup.find(id=hari).find("span", {"data-testid": "SunsetTime", "class": "DetailsTable--value--1q_qD"})

    Kecepatan_angin = soup.find(id=hari).find("span", {"data-testid": "Wind", "class": "Wind--windWrapper--3aqXJ DailyContent--value--37sk2"})

    perkiraan = soup.find(id=hari).find("div", {"data-testid": "wxIcon", "class": "DetailsSummary--condition--24gQw"})
    
    #Â°
   
    Mat_ter = str(Matahari_terbit)
    Mat_terben = str(Matahari_terbenam)
    char_1 = '">'
    char_2 = '</'
    Mat_ter = Mat_ter[Mat_ter.find(char_1) + 2 : Mat_ter.find(char_2)]
    Mat_terben = Mat_terben[Mat_terben.find(char_1) + 2 : Mat_terben.find(char_2)]


    df.loc[n] = [waktu.text, 
    temp_data_siang.text[:2], 
    temp_data_malam.text[:2], 
    uv_index.text, 
    bulan_terbenam.text, 
    bulan_terbit.text,
    Fase_bulan.text, 
    Mat_ter, 
    Mat_terben, 
    Kecepatan_angin.text, 
    humid.text, 
    perkiraan.text]
    n = n+1
    
    
print(df)

df.to_csv(r'C:/Users/P5CD1/OneDrive/Documents/GitHub/DataScience_Discuss/Parsing_weather.csv', index = False)


# Credentials to database connection
hostname="localhost"
dbname="workshop"
uname="root"
pwd="sanjii123"


# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))

# Convert dataframe to sql table                                   
df.to_sql('cuaca_current', engine, if_exists='replace', index=False)
df.to_sql('cuaca_hystorian', engine, if_exists='append', index=False)
df