import requests
from bs4 import BeautifulSoup
import pandas as pd
import pandas as pd
from IPython.display import display

#------Pakai proxy kantor
#url = "http://192.168.17.65/kinerja-operasi/public/telemetri"
#r = requests.get(url,verify=False)
#soup = BeautifulSoup(r.content, "lxml")
#------------------------


#------Testing pakai saving html
url = "C:/Users/P5CD1/OneDrive/Documents/GitHub/DataScience_Discuss/DS_test/Scrapping_telemetriBebanUPMKR/web_telemetriUPMKR.html"
page = open(url)
soup = BeautifulSoup(page.read())
#---------------------------------


df_01 = list()
for el in soup.find_all("div",{"class" : "container-fluid"}):
    df_01.append(el.get_text("\n",strip=True).split("\n"))

df_01 = pd.DataFrame(df_01)

df_02 = pd.read_csv('C:/Users/P5CD1/OneDrive/Documents/GitHub/DataScience_Discuss/DS_test/Scrapping_telemetriBebanUPMKR/data_telemetriBeban_UPMKR.csv')

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

df_02.to_csv("C:/Users/P5CD1/OneDrive/Documents/GitHub/DataScience_Discuss/DS_test/Scrapping_telemetriBebanUPMKR/data_telemetriBeban_UPMKR.csv", index = False)



