import numpy as np
import pandas as pd

from datetime import date, time

def Get_temperature(year, region):
    '''
    Year (list): 
    2016 / 2017 / 2018 / 2019 / 2020 / 2021 / 2022

    Region (str): 
    AURA / Bourgogne / Bretagne / Centre / GrandEst / HautsDeFrance / IDF / Normandie / NouvelleAquitaine / Occitanie / PACA / PaysDeLoire
    '''

    #Numéro de station météo par région
    station = {
        "AURA" : 7481,
        "Bourgogne" : 7280,
        "Bretagne" : 7130,
        "Centre" : 7240,
        "GrandEst" : 7190,
        "HautsDeFrance" : 7015,
        "IDF" : 7149,
        "Normandie" : 7037,
        "NouvelleAquitaine" : 7510,
        "Occitanie" : 7630,
        "PACA" : 7650,
        "PaysDeLoire" : 7222
    }
    data = pd.DataFrame()

    #Lecture des fichiers
    for i,year in enumerate(year):
        for j in range(1,13):
            if len(str(j))==1:
                df = pd.read_csv(f'https://raw.githubusercontent.com/Tdjaaleb/MALIA/main/Time%20Series/Raw%20Data/Temperature/{year}/0{j}%20{year}.csv', sep=';')
            if len(str(j))==2:
                df = pd.read_csv(f'https://raw.githubusercontent.com/Tdjaaleb/MALIA/main/Time%20Series/Raw%20Data/Temperature/{year}/{j}%20{year}.csv', sep=';')

            df = pd.concat([df["date"].where(df["numer_sta"]==station[region]), df["t"].where(df["numer_sta"]==station[region])], axis=1).dropna()
            
            #Conversion en degré Celsius
            df["t"] = df["t"].replace("mq", np.NaN)
            df["Temperature"] = df["t"].astype("float64")-273.15

            #Recodage de la Date et de l'heure
            Date = []
            Heure = []
            temp = []
            l=0
            for k,obs in enumerate((df["date"].astype("int64")).astype(str)):
                Date.append(date.fromisoformat(obs[0:4]+'-'+obs[4:6]+'-'+obs[6:8]))
                Heure.append(time.fromisoformat(obs[8:10]+':'+obs[10:12]+':'+obs[12:14]))
                temp.append(df["Temperature"][df.index[l]])
                l=l+1
                if (Date[-1]==date(2022,12,1)) & (Heure[-1]==time(0,0,0)):
                    break

            to_add = pd.DataFrame({
                "Date" : Date,
                "Heure" : Heure,
                "Temperature" : temp
            })
            df = df.drop(["t", "date"], axis=1)
            data = pd.concat([data,to_add])
            
    #Réindexage   
    ind = []
    for i in range(data.shape[0]):
        ind.append(i)
    data.index = ind

    return data

