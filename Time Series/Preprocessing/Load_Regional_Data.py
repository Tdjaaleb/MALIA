import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

def Get_regional_data(year, region):
    '''
    Year (list): 
    2016 / 2017 / 2018 / 2019 / 2020 / 2021-2022-1 / 2022-2

    Region (str): 
    AURA / Bourgogne / Bretagne / Centre / GrandEst / HautsDeFrance / IDF / Normandie / NouvelleAquitaine / Occitanie / PACA / PaysDeLoire
    '''
    
    data = pd.DataFrame()

    to_drop = ["Perimetre", "Nature", "Thermique", "Nucleaire", "Eolien", "Solaire", "Hydraulique", "Pompage", "Bioenergies", "Ech. physiques"]

    #Lecture des fichiers
    for i,year in enumerate(year):
        df = pd.read_csv(f'https://raw.githubusercontent.com/Tdjaaleb/MALIA/main/Time%20Series/Raw%20Data/Energy/Regional/{region}/{region}-{year}.csv', sep=";")
        df = df.drop(to_drop, axis=1)
        df = df.dropna()
        data = pd.concat([data,df])

    ind = []
    for i in range(data.shape[0]):
        ind.append(i)
    data.index = ind

    #Interpolation des valeurs manquantes (consommation)
    data = data.replace("ND", np.NaN)
    data["Consommation"] = data["Consommation"].astype("float64")

    conso = [data["Consommation"][0]]
    interpolation = interp1d(data.dropna().index, data["Consommation"].dropna(), kind='cubic')
    xnew = np.linspace(0, data.shape[0]-1, num=data.shape[0], endpoint=True)
    for i in range(1,xnew.shape[0]):
            conso.append(round(float(interpolation(xnew[i])), 0))

    data["Consommation"] = conso

    #Suppression des données recueillies à 15min et 45min
    for i in range(data.shape[0]):
        if i>=data.shape[0]-1:
            break
        if data["Heures"][i][4:5]=='5':
            data = data.drop(labels=data.index[i], axis=0)
            data = data.sort_index().reset_index(drop=True)
    if data["Heures"][data.shape[0]-1][4:5]=='5':
        data = data.drop(labels=data.index[data.shape[0]-1], axis=0)
        data = data.sort_index().reset_index(drop=True)
    
    return data