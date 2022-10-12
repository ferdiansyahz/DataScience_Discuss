import requests
from bs4 import BeautifulSoup

url = "https://weather.com/id-ID/weather/tenday/l/Kramat+Daerah+Khusus+Ibukota+Jakarta?canonicalCityId=9d5f83a2a29b1f4aa5272fca53aa871b328c5ee66f6882d07480f0a94b37565c#detailIndex5"

r = requests.get(url,verify=False)

soup = BeautifulSoup(r.content, "lxml")

#g_data = soup.find("div", {"data-testid":"ConditionsSummary", "class":"DailyContent--ConditionSummary--1X5kT"})

#g_data = soup.find("span", {"data-testid": "TemperatureValue", "class": "DailyContent--temp--3d4dn"})

temp_data_0 = soup.find(id="detailIndex0").find("span", {"data-testid": "TemperatureValue", "class": "DailyContent--temp--3d4dn"})
temp_data_1 = soup.find(id="detailIndex1").find("span", {"data-testid": "TemperatureValue", "class": "DailyContent--temp--3d4dn"})

humid_data_0 = soup.find(id="detailIndex0").find("span", {"data-testid": "PercentageValue", "class": "DetailsTable--value--1q_qD"})
humid_data_1 = soup.find(id="detailIndex1").find("span", {"data-testid": "PercentageValue", "class": "DetailsTable--value--1q_qD"})

print("\n----Data Dari Weather.com----")
print("\nArea DKI Jakarta")

print("\nTemperature Hari Ini : ")
print(temp_data_0.text)
print("Humidity Hari ini : ")
print(humid_data_0.text)

print("Temperature Besok : ")
print(temp_data_1.text)
print("Humidity Besok : ")
print(humid_data_1.text)
print("\n")