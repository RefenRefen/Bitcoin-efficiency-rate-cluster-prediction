from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

class Clustering:
    def __init__(self, df_dict, plot: bool = False):
        self.df_dictionary = df_dict
        self.plot = plot

    def efficiency_rate_clustering(self):
        dfs = list()
        dfs_name = list()
        for name, data_frame in self.df_dictionary.items():
            dfs.append(data_frame)
            dfs_name.append(name)

        for i in dfs:

            for j in i.columns[1:]:
                ini_array = i[j]
                ini_array = np.array(ini_array)
                ini_array = [i if i >= 0 else np.nan for i in ini_array]
                i[j] = ini_array
            i.insert(i.columns.shape[0], "efficiency_rate", (i['close'] - i['open']) / i['open'], True)
        j = 0
        return_dict = dict()
        for df in dfs:
            rate_array = np.array(df['efficiency_rate'])
            rate_array = np.nan_to_num(rate_array, copy=True, nan=0.0, posinf=None, neginf=None)
            for i in range(2):
                rate_array = np.where(rate_array == rate_array[rate_array.argmax()], 0, rate_array)
                rate_array = np.where(rate_array == rate_array[rate_array.argmin()], 0, rate_array)
            rate_array = np.array(rate_array).reshape(-1, 1)

            model = KMeans(init='k-means++', n_clusters=3, random_state=0)
            model.fit(rate_array)
            clusters_predict = model.predict(rate_array)

            if self.plot:
                fig, ax = plt.subplots(figsize=(8, 6))
                ax.scatter(rate_array, [1 for i in range(rate_array.shape[0])], s=50, c=clusters_predict, cmap='viridis')
                ax.set_xlabel('Efficiency Rate')
                ax.set_title(dfs_name[j] + ' clusters')
                plt.show()

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
            return_dict[dfs_name[j]] = df
            j += 1
        return return_dict
