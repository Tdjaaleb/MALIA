import pandas as pd

def Get_national_data(year):
    data = pd.DataFrame()

    to_drop = ["Perimetre", "Nature", "Prevision J-1","Prevision J", "Fioul", "Charbon", "Gaz",
"Nucleaire", "Eolien", "Solaire", "Hydraulique","Pompage", "Bioenergies", "Ech. physiques",
"Taux de Co2", "Ech. comm. Angleterre","Ech. comm. Espagne", "Ech. comm. Italie","Ech. comm. Suisse",
"Ech. comm. Allemagne-Belgique", "Fioul - TAC", "Fioul - Cogen.", "Fioul - Autres", "Gaz - TAC",
"Gaz - Cogen.", "Gaz - CCG", "Gaz - Autres", "Hydraulique - Fil de l?eau + eclusee", "Hydraulique - Lacs",
"Hydraulique - STEP turbinage", "Bioenergies - Dechets", "Bioenergies - Biomasse", "Bioenergies - Biogaz"]

    for i,year in enumerate(year):
        df = pd.read_csv(f'https://raw.githubusercontent.com/Tdjaaleb/MALIA/main/Time%20Series/Raw%20Data/Energy/National/{year}.csv', sep=";")
        df = df.drop(to_drop, axis=1)
        df = df.dropna()
        data = pd.concat([data,df])
    ind = []
    for i in range(data.shape[0]):
        ind.append(i)
    data.index = ind
    return data

year = ["2016","2017","2018","2019","2020","2021-2022-1","2022-2"]

df = Get_national_data(year)