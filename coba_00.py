import requests
from bs4 import BeautifulSoup as bs

url = "https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-DKIJakarta.xml"
response = requests.get(url,verify=False)
r = response.text

prakiraan = {'Pagi': '' , 'Siang': '', 'Malam': ''}
kode = {
'0': 'Cerah / Clear Skies',
'1': 'Cerah Berawan / Party Cloudy',
'2': 'Cerah Berawan / Partly Cloudy',
'3': 'Berawan / Mostly Cloudy',
'4': 'Berawan Tebal / Overcast',
'5': 'Udara Kabur / Haze',
'10': 'Asap / Smoke',
'45': 'Kabut / Fog',
'60': 'Hujan Ringan / Light Rain',
'61': 'Hujan Sedang / Rain',
'63': 'Hujan Lebat / Heavy Rain',
'80': 'Hujan Lokal / Isolated Shower',
'95': 'Hujan Petir / Severe Thunderstorm',
'97': 'Hujan Petir / Severe Thunderstorm'
}

DKIjakarta = bs(r,"xml")

#CuacaJakartaUtara
cuacaJakut = DKIjakarta.find(id="501196").find(id="weather")

h0 = cuacaJakut.find(h='0').value.string
h6 = cuacaJakut.find(h='6').value.string
h12 = cuacaJakut.find(h='12').value.string

prakiraan['Pagi'] = kode[h0]
prakiraan['Siang'] = kode[h6]
prakiraan['Malam'] = kode[h12]

#humididyJakut
humidJakut = DKIjakarta.find(id="501196").find(id="hu")
humid_pagi = humidJakut.find(h='0').value.string
humid_siang = humidJakut.find(h='6').value.string
humid_malam = humidJakut.find(h='12').value.string


#TemperatureJAKUT
TempJakut = DKIjakarta.find(id="501196").find(id="t")
temp_pagi = TempJakut.find(h='0').value.string
temp_siang = TempJakut.find(h='6').value.string
temp_malam = TempJakut.find(h='12').value.string


print(
	"BMKG JAKARTA UTARA HARI INI",
	"\nid=501196"
	"\nPagi  : ",
	prakiraan['Pagi'],
	"\nSiang : ",
	prakiraan['Siang'],
	"\nMalam : ",
	prakiraan['Malam'],
	
	"\nHumidity Pagi : ",
	humid_pagi,
	"\nHumidity Siang : ",
	humid_siang,
	"\nHumidity Malam : ",
	humid_malam,
	"\nTemperatur Pagi: ",
	temp_pagi,
	"\nTemperatur Siang: ",
	temp_siang,
	"\nTemperatur Malam: ",
	temp_malam
	)