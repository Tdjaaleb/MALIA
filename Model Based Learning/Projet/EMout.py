import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt

#--------------------------------------------------------CLASS : MODEL------------------------------------------------------------------
class Model:
    def __init__(self, data, uniform, tik, log_likelihood, bic, params):
        from EMout import map

        self.data = data
        self.uniform = uniform
        self.tik = tik
        self.clusters = map(tik)
        self.log_likelihood = log_likelihood
        self.bic = bic
        self.params = params
    
    def __str__(self):
        print("---------------------------------------------------------------")
        print("Présence d'une loi uniforme : ",self.uniform)
        print("---------------------------------------------------------------")
        print("Clusters :")
        print(self.clusters)
        print("---------------------------------------------------------------")
        print("Log Likelihood finale : ", self.log_likelihood[-1])
        print("---------------------------------------------------------------")
        print("Valeur du critère BIC : ", self.bic)
        print("---------------------------------------------------------------")
        return "Algorithm EMout for outliers detection in clustering"
    
    def plot(self):
        for i in range(self.data.shape[1]-1):
            for j in range(self.data.shape[1]-1):
                if i<j+1:
                    plt.figure()
                    plt.scatter(self.data[:,i], self.data[:,1+j],c=self.clusters)
                    plt.xlabel("Var "+str(i))
                    plt.ylabel("Var "+str(1+j))
    
    def plot_llh(self):
      plt.figure()
      plt.plot(self.log_likelihood)
      plt.xlabel("Itérations")
      plt.ylabel("Log Likelihood")

#--------------------------------------------------------DEF : E------------------------------------------------------------------
def E(data, clusters, mu, Sigma, p, tik, log_likelihood):
    n = data.shape[0]
    k = clusters
    
    tik_update = tik
    log_update = log_likelihood

    #Fonction représentant f_k(x)
    def PDF(mean,cov):
      return(multivariate_normal.pdf(data,mean,cov, allow_singular=True))

    #Mise à jour des tik (numérateur)
    for i in range(k):
      tik_update[:, i] = p[i] * PDF(mu[i], Sigma[i])

    llh = np.sum(np.log(np.sum(tik_update, axis = 1)))
    log_update = np.append(log_likelihood, llh)

    #Division par la somme des pk*fk
    for i in range(n):
      S = np.sum(tik_update[i,:])
      tik_update[i,:] = tik_update[i,:]/S

    return tik_update, log_update

#--------------------------------------------------------DEF : M------------------------------------------------------------------
def M(data, clusters, mu, Sigma, p, tik):
    n = data.shape[0]
    k = clusters
    nk = np.sum(tik, axis = 0)

    Sigma_update = Sigma
    p_update = p
    mu_update = mu

    for i in range(k):
      #Maj de Sigma
      Sigma_update[i] = ((tik[:,i] * ((data - mu[i]).T)) @ (data - mu[i])) / nk[i]
      #Maj de p
      p_update[i] = nk[i] / n
      #Maj de mu
      mu_update[i] = (1. / nk[i]) * np.sum(tik[:,i] * data.T, axis = 1).T 

    return Sigma_update, p_update, mu_update

#--------------------------------------------------------DEF : EOUT------------------------------------------------------------------
def Eout(data, clusters, mu, Sigma, p, tik, log_likelihood):
    n = data.shape[0]
    k = clusters
    
    uni = 1
    for i in range(data.shape[1]):
        uni = uni*(data[:,i].max()-data[:,i].min())
    
    pdf_uni = 1/uni

    tik_update = tik
    log_update = log_likelihood

    #Fonction représentant f_k(x)
    def PDF(mean,cov):
      return(multivariate_normal.pdf(data,mean,cov,allow_singular=True))

    #Mise à jour des tik (numérateur)
    for i in range(k):
      tik_update[:, i] = p[i] * PDF(mu[i], Sigma[i])

    tik_update[:,k] = p[k] * pdf_uni

    llh = np.sum(np.log(np.sum(tik_update, axis = 1)))
    log_update = np.append(log_likelihood, llh)

    #Division par la somme des pk*fk
    for i in range(n):
      S = np.sum(tik_update[i,:])
      tik_update[i,:] = tik_update[i,:]/S

    return tik_update, log_update, pdf_uni

#--------------------------------------------------------DEF : MOUT------------------------------------------------------------------
def Mout(data, clusters, mu, Sigma, p, tik):
    n = data.shape[0]
    k = clusters
    nk = np.sum(tik, axis = 0)

    Sigma_update = Sigma
    p_update = p
    mu_update = mu

    for i in range(k):
      #Maj de Sigma
      Sigma_update[i] = ((tik[:,i] * ((data - mu[i]).T)) @ (data - mu[i])) / nk[i]
      #Maj de p
      p_update[i] = nk[i] / n
      #Maj de mu
      mu_update[i] = (1. / nk[i]) * np.sum(tik[:,i] * data.T, axis = 1).T 

    p_update[k] = nk[k]/n

    return Sigma_update, p_update, mu_update

#--------------------------------------------------------DEF : MAP------------------------------------------------------------------
def map(tik):
    classes=np.empty(0, dtype=int)
    for i in range(tik.shape[0]):
        classes = np.append(classes,(np.where(tik[i] == np.max(tik[i]))))
    return classes

#--------------------------------------------------------DEF : PARAM INIT------------------------------------------------------------------
def param_init(init, data, clusters, uni=False):
    
    n = data.shape[0]
    dims = data.shape[1]
    k = clusters
    llh = -10**100
    mu = data[np.random.choice(n,k,replace = False)]
    Sigma = np.full((k,dims,dims),np.eye(dims)*100)
    log_likelihood = np.empty((0,))
    

    if uni==False:
        p = np.full(k, 1/k)
        tik = np.zeros((n,k))

        for i in range(init):
            for j in range(10):
                tik, log_likelihood = E(data, clusters, mu, Sigma, p, tik, log_likelihood)
                Sigma, p, mu = M(data, clusters, mu, Sigma, p, tik)
            if log_likelihood[-1]>llh:
                llh = log_likelihood[-1]
                mu_init = mu
                Sigma_init=Sigma
                p_init = p
                tik_init = tik
    else:
        p = np.full(k+1, 1/(k+1))
        tik = np.zeros((n,k+1))
        
        for i in range(init):
            for j in range(10):
                tik, log_likelihood, pdf_uni = Eout(data, clusters, mu, Sigma, p, tik, log_likelihood)
                Sigma, p, mu = Mout(data, clusters, mu, Sigma, p, tik)
            if log_likelihood[-1]>llh:
                llh = log_likelihood[-1]
                mu_init = mu
                Sigma_init=Sigma
                p_init = p
                tik_init = tik
    return mu_init, Sigma_init, p_init, tik_init

#--------------------------------------------------------DEF : EM------------------------------------------------------------------
def EM(data, clusters, iter, init=20):
    from EMout import Model,E,M,Eout,Mout,param_init

    n = data.shape[0]
    dims = data.shape[1]
    k = clusters

    #-------------------MODELE 1-------------------------
    #Initialisation de mu, Sigma, p, tik, llh

    mu, Sigma, p, tik = param_init(init=init, data=data, clusters=clusters)    
    log_likelihood = np.empty((0,))
    
    for i in range(iter):
      tik, log_likelihood = E(data, clusters, mu, Sigma, p, tik, log_likelihood)
      Sigma, p, mu = M(data, clusters, mu, Sigma, p, tik)

    bic_base = 2*log_likelihood[-1]-(dims**2+k)*np.log(n)

    #-------------------MODELE 2-------------------------
    #Initialisation de mu, Sigma, p, tik, llh
    mu_uni, Sigma_uni, p_uni, tik_uni = param_init(init=init, data=data, clusters=clusters, uni=True)    
    log_likelihood_uni = np.empty((0,))
    
    for i in range(iter):
      tik_uni, log_likelihood_uni, pdf_uni = Eout(data, clusters, mu_uni, Sigma_uni, p_uni, tik_uni, log_likelihood_uni)
      Sigma_uni, p_uni, mu_uni = Mout(data, clusters, mu_uni, Sigma_uni, p_uni, tik_uni)

    bic_uni = 2*log_likelihood_uni[-1]-(dims**2+k+2*dims)*np.log(n)
    
    #----------------Selection du modèle----------------
    if bic_base > bic_uni:
      params_base = {"Sigma" : Sigma, "Mu" : mu, "p" : p}
      ans = Model(data=data, uniform=False, tik=tik, log_likelihood=log_likelihood, bic=bic_base, params=params_base)
    else :
      params_uni = {"Sigma" : Sigma_uni, "Mu" : mu_uni, "p" : p_uni, "pdf_uni" : pdf_uni}
      ans = Model(data=data, uniform=True, tik=tik_uni, log_likelihood=log_likelihood_uni, bic=bic_uni, params=params_uni)
      
    print(ans)
    return ans
