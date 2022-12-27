import pandas as pd
import numpy as np

def Get_regional_data(year, region):
    '''
    Year (list): 
    2016 / 2017 / 2018 / 2019 / 2020 / 2021-2022-1 / 2022-2

    Region (str): 
    AURA / Bourgogne / Bretagne / Centre / GrandEst / HautsDeFrance / IDF / Normandie / NouvelleAquitaine / Occitanie / PACA / PaysDeLoire
    '''
    
    data = pd.DataFrame()

    to_drop = ["Perimetre", "Nature", "Thermique", "Nucleaire", "Eolien", "Solaire", "Hydraulique", "Pompage", "Bioenergies", "Ech. physiques"]

    for i,year in enumerate(year):
        df = pd.read_csv(f'https://raw.githubusercontent.com/Tdjaaleb/MALIA/main/Time%20Series/Raw%20Data/Energy/Regional/{region}/{region}-{year}.csv', sep=";")
        df = df.drop(to_drop, axis=1)
        df = df.dropna()
        data = pd.concat([data,df])

    ind = []
    for i in range(data.shape[0]):
        ind.append(i)
    data.index = ind

    data = data.replace("ND", np.NaN)
    data["Consommation"] = data["Consommation"].astype("float64")
    
    return data
