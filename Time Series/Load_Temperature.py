import numpy as np
import pandas as pd

def Get_temperature(year, region):
    '''
    Year (list): 
    2016 / 2017 / 2018 / 2019 / 2020 / 2021 / 2022

    Region (str): 
    AURA / Bourgogne / Bretagne / Centre / GrandEst / HautsDeFrance / IDF / Normandie / NouvelleAquitaine / Occitanie / PACA / PaysDeLoire
    '''


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

    for i,year in enumerate(year):
        for j in range(1,13):
            if len(str(j))==1:
                df = pd.read_csv(f'https://raw.githubusercontent.com/Tdjaaleb/MALIA/main/Time%20Series/Raw%20Data/Temperature/{year}/0{j}%20{year}.csv', sep=';')
            if len(str(j))==2:
                df = pd.read_csv(f'https://raw.githubusercontent.com/Tdjaaleb/MALIA/main/Time%20Series/Raw%20Data/Temperature/{year}/{j}%20{year}.csv', sep=';')

            df = pd.concat([df["date"].where(df["numer_sta"]==station[region]), df["t"].where(df["numer_sta"]==station[region])], axis=1).dropna()
            
            #Recodage de la Date et de l'heure
            Date = []
            Heure = []
            for k,obs in enumerate((df["date"].astype("int64")).astype(str)):
                Date.append(obs[6:8]+"/"+obs[4:6]+"/"+obs[0:4])
                Heure.append(obs[8:10]+":"+obs[10:12])
            df["Date"] = Date
            df["Heure"] = Heure

            #Conversion en degré Celsius
            df["t"] = df["t"].replace("mq", np.NaN)
            df["Temperature"] = df["t"].astype("float64")-273.15
            
            df = df.drop(["t", "date"], axis=1)
            data = pd.concat([data,df])
       
    ind = []
    for i in range(data.shape[0]):
        ind.append(i)
    data.index = ind

    return data