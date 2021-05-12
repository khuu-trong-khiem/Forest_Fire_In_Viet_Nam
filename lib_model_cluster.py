from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sb

def getKmeanOptimal(data, k):
    kmeanModel = KMeans(n_clusters=k, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeanModel.fit(data)
    return sum(
        np.min(
            cdist(
                data, 
                kmeanModel.cluster_centers_,
                "euclidean"
            ),
            axis=1
        )
    ) / data.shape[0]

def getGMMScore(data, k):
    gmm = GaussianMixture(n_components=k)
    gmm.fit(data)
    labels = gmm.predict(data)
    return metrics.silhouette_score(
        data, 
        labels,
        metric='euclidean'
    )

def showTestKMean(data, number, title = ''):
    list_n = []
    list_kmean = []
    for n in range(1, number):
        list_n.append(n)
        list_kmean.append(
            getKmeanOptimal(data, n)
        )
    table = pd.DataFrame({
        'N': list_n,
        'KMean': list_kmean
    })
    plt.grid(True)
    plt.plot(table.N, table.KMean, 'ro-', label='KMean')
    plt.xlabel('K')
    plt.ylabel('WSSSE')
    plt.title(title, loc='left', fontweight='bold')
    plt.show()

def showTestCluster(data, number, title = ''):
    list_n = []
    list_gmm = []
    list_kmean = []
    for n in range(2, number):
        list_n.append(n)
        list_kmean.append(
            getKmeanOptimal(data, n)
        )
        list_gmm.append(
            getGMMScore(data, n)
        )
    df = pd.DataFrame({
        'GMM': list_gmm,
        'KMean': list_kmean
    })
    scaler = MinMaxScaler()
    re = scaler.fit(df).transform(df)
    table = pd.DataFrame({
        'N': list_n,
        'GMM': re[:, 0],
        'KMean': re[:, 1]
    })
    plt.grid(True)
    plt.plot(table.N, table.GMM, 'bo-', label='GMM')
    plt.plot(table.N, table.KMean, 'ro-', label='KMean')
    plt.xlabel('N')
    plt.ylabel('Distortions')
    plt.legend()
    plt.title(title, loc='left', fontweight='bold')
    plt.show()