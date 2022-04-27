import numpy as np
from sklearn.cluster import KMeans, AgglomerativeClustering
import pandas as pd
import requests
import datetime
import json
import matplotlib.pyplot as plt
from sklearn import preprocessing as sp
from sklearn.preprocessing import Normalizer

gold_query = '''query {
  golds {
    date
    high
    low
    open
    volume
    close
  }
}'''

crude_oil_query = '''query {
  crudeOils {
    date
    high
    low
    open
    volume
    close
  }
}'''

bitcoin_query = '''query {
  bitcoins {
    date
    high
    low
    open
    volume
    close
  }
}'''
queries = list()
queries.append(gold_query)
queries.append(bitcoin_query)
queries.append(crude_oil_query)

df_name = ['gold', 'bitcoin', 'crude_oil']
df_dictionary = dict()

for k in range(len(queries)):
    file = requests.get('http://localhost:4000/graphql'
                        '?query={q}'.format(q=queries[k]))
    x = file.text.split('{')
    x = x[2:]
    records = list()
    for i in range(len(x)):
        dictionary = json.loads('{' + x[i][:-2])
        records.append(dictionary)
    df = pd.DataFrame.from_records(records)
    df = df.astype(
        {"high": float, "low": float, 'open': float, 'volume': float, 'close': float})
    df['date'] = pd.to_datetime(df['date'])
    df_dictionary[df_name[k]] = df

dfs = list()
for name, data_frame in df_dictionary.items():
    dfs.append(data_frame)

# gold_bitcoin_df = dfs[0].join(dfs[1].set_index('date'), lsuffix='_gold', rsuffix='_bitcoin', on='date')

for i in dfs:
    i.insert(i.columns.shape[0], "efficiency_rate", i['close'] / i['open'], True)

for df in dfs:
    rate_array = np.array(df['efficiency_rate'])
    rate_array = [1 if i < 0 else i for i in rate_array]
    rate_array = np.array(rate_array).reshape(-1, 1)
    rate_array = np.nan_to_num(rate_array, copy=True, nan=1.0, posinf=None, neginf=None)

    model = KMeans(init='k-means++', n_clusters=3, random_state=0)
    model.fit(rate_array)
    clusters_predict = model.predict(rate_array)

    # print(model.cluster_centers_)

    '''Mapping Clusters'''
    cluster_centers = list()
    for i in model.cluster_centers_:
        cluster_centers.append(i[0])

    min_label = model.predict([[min(cluster_centers)]])[0]
    max_label = model.predict([[max(cluster_centers)]])[0]

    cluster = list()
    for i in clusters_predict:
        if i == min_label:
            cluster.append(-1)
        elif i == max_label:
            cluster.append(1)
        else:
            cluster.append(0)
    df.insert(df.columns.shape[0], "efficiency_cluster", cluster, True)

# print(x)
# fig, ax = plt.subplots(figsize=(8, 6))
# ax.scatter(rate_array, [1 for i in range(rate_array.shape[0])], s=50, c=x, cmap='viridis')
# plt.show()

for i in dfs:
    print(i.tail())
