import numpy as np
import pandas as pd
from datetime import date, time
from scipy.interpolate import interp1d

#--------------------------------------------------------------------------------COMPLETE TEMP DATE
def Complete_Temp_Date(df, period=20209):
    '''
    df (pandas.DataFrame)

    period (int)
    '''
    df = df.drop_duplicates()
    df = df.sort_values(by=["Date","Heure"]).reset_index(drop=True)
    data = df.copy(deep=False)
    
    #Création d'observations manquantes pour les températures 
    for i in range(period-1):
        if data["Date"][i]==data["Date"][i+1]:
            if data["Heure"][i+1].hour - data["Heure"][i].hour !=3:
                data.loc[i+0.5] = [data["Date"][i],time(data["Heure"][i].hour+3,0,0), np.NaN]
                data = data.sort_index().reset_index(drop=True)
                continue

        if data["Date"][i]!=data["Date"][i+1]:
            if data["Heure"][i+1].hour - data["Heure"][i].hour !=-21:
                if data["Heure"][i].hour < 21:
                    data.loc[i+0.5] = [data["Date"][i],time(data["Heure"][i].hour+3,0,0), np.NaN]
                    data = data.sort_index().reset_index(drop=True)
                    continue
                else:
                    data.loc[i+0.5] = [data["Date"][i]+date.resolution,time(0,0,0), np.NaN]
                    data = data.sort_index().reset_index(drop=True)
                    continue
    
    #Réindexage
    data = data.sort_index().reset_index(drop=True)
    return data

#--------------------------------------------------------------------------------TEMP INTERPOLATION
def temp_interpolation(df):
    '''
    df (pandas.DataFrame)
    '''
    data = df.copy(deep=False)

    Date = [data["Date"][0]]
    Heure = [data["Heure"][0]]
    temp = [data["Temperature"][0]]

    #Interpolation des températures pour obtenir des observations toutes les 30min
    interpolation = interp1d(data.dropna().index, data["Temperature"].dropna(), kind='cubic')
    xnew = np.linspace(0, data.shape[0]-1, num=data.shape[0]*6-5, endpoint=True)

    for i in range(1,xnew.shape[0]):
        if (Heure[-1].hour==23) & (Heure[-1].minute==30):
            Date.append(Date[-1]+date.resolution)
            Heure.append(time(0,0,0))
            temp.append(round(float(interpolation(xnew[i])), 2))
        else:
            if Heure[-1].minute==30:
                Date.append(Date[-1])
                Heure.append(time(Heure[-1].hour+1,0,0))
                temp.append(round(float(interpolation(xnew[i])), 2))
            elif Heure[-1].minute==0:
                Date.append(Date[-1])
                Heure.append(time(Heure[-1].hour,30,0))
                temp.append(round(float(interpolation(xnew[i])), 2))
    
    data = pd.DataFrame({
        "Date" : Date,
        "Heure" : Heure,
        "Temperature" : temp
    })

    return data