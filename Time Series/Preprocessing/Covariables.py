import numpy as np
import pandas as pd

#--------------------------------------------------------------------------------COVARIABLES
def covariables(temperature, conso, jours=2526, data="regional"):
    '''
    temperature (pandas.DataFrame)

    conso (pandas.DataFrame)

    jours (int)

    data (str)
    "regional" /  "national"
    '''
    temp = temperature.copy(deep=False)

    #Création des covariables tod (time of day) et tow(time of week)
    tod = np.linspace(0, 1, num=48, endpoint=True)

    cov_tod = np.empty((0,))
    cov_tow = np.empty((0,))
    
    tow = 4/6
    for i in range(jours):
        day = np.full((48,), tow)
        cov_tod = np.concatenate((cov_tod , tod))
        cov_tow = np.concatenate((cov_tow, day))
        if tow<0.98:
            tow = tow+1/6
        else:
            tow = 0

    cov_tow = np.append(cov_tow, 0.5)
    cov_tod = np.append(cov_tod, 0)

    #Création des variables t-1, j-1, j-7
    j1 = conso["Consommation"].shift(periods=48)
    j7 = conso["Consommation"].shift(periods=336)
    t1 = conso["Consommation"].shift(periods=1)

    temp["tod"] = cov_tod
    temp["tow"] = cov_tow
    temp["ConsoJ-1"] = j1
    temp["ConsoJ-7"] = j7
    temp["ConsoT-1"] = t1
    temp["Conso"] = conso["Consommation"]

    if data == "national":
        temp = temp.drop("Temperature", axis=1)
    
    temp = temp.drop(temp.tail(1).index)

    return temp

#--------------------------------------------------------------------------------FFT DENOISER
def fft_denoiser(x, n_components = 10000000000, to_real=True):
    '''
    x (np.array)

    n_components (int)

    to_real (boolean)
    '''
    #https://www.youtube.com/watch?v=s2K1JfNR7Sc&ab_channel=SteveBrunton

    n = len(x)

    #compute the fft
    fft = np.fft.fft(x, n)
    
    #compute power spectrum density
    #squared magnitud of each fft coefficient
    PSD = fft * np.conj(fft) / n

    #keep high frequencies
    _mask = PSD > n_components
    fft = _mask * fft

    #inverse fourier transform
    clean_data = np.fft.ifft(fft)

    if to_real:
        clean_data = clean_data.real

    return clean_data
