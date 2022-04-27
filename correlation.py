import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


class Correlation:
    def __init__(self, lead_lag: int, currency_pair: list, currency_dict: dict):
        self.lead_lag = lead_lag
        self.currency_pair = currency_pair
        self.currency_dict = currency_dict

    def correlation(self):
        lag_lead_list = [i for i in range(-self.lead_lag, self.lead_lag + 1)]
        lag_lead_list.remove(0)

        dfs = list()
        dfs_name = list()
        for name, data_frame in self.currency_dict.items():
            if name in self.currency_pair:
                dfs.append(data_frame)
                dfs_name.append(name)

        for i in dfs:
            for j in i.columns[1:]:
                ini_array = i[j]
                ini_array = np.array(ini_array)
                ini_array = [i if i >= 0 else np.nan for i in ini_array]
                i[j] = ini_array
            i.insert(i.columns.shape[0], "efficiency_rate", (i['close'] - i['open']) / i['open'], True)

        joined_df = dfs[0].join(dfs[1].set_index('date'), lsuffix='_{c}'.format(c=dfs_name[0]),
                                rsuffix='_{c}'.format(c=dfs_name[1]), on='date')

        new_df = pd.DataFrame()
        new_df['{c}_rate'.format(c=dfs_name[0])] = joined_df['efficiency_rate_{c}'.format(c=dfs_name[0])]
        new_df['{c}_rate'.format(c=dfs_name[1])] = joined_df['efficiency_rate_{c}'.format(c=dfs_name[1])]
        new_df = new_df.dropna()

        for curr in dfs_name:
            for i in lag_lead_list:
                if i > 0:
                    new_df[curr + '(+{lg_ld})'.format(lg_ld=i)] = new_df['{c}_rate'.format(c=curr)].shift(i)
                else:
                    new_df[curr + '({lg_ld})'.format(lg_ld=i)] = new_df['{c}_rate'.format(c=curr)].shift(i)

        new_df = new_df.dropna()

        plt.figure(figsize=(15, 10))
        plt.title(u'{l} lead-lag correlation between {c1} and {c2}'.format(l=self.lead_lag,
                                                                           c1=self.currency_pair[1],
                                                                           c2=self.currency_pair[0]),
                  y=1.05, size=16)
        mask = np.zeros_like(new_df.corr())
        mask[np.triu_indices_from(mask)] = True
        sns.set(font_scale=0.6)
        svm = sns.heatmap(new_df.corr(), mask=mask, linewidths=0.1, vmax=1.0,
                          square=True, linecolor='white', annot=True)
        plt.show()
