import copy
import correlation
from prediction import Model
from clustering import Clustering
from graphqlrequest import GraphQLRequest

url = 'http://localhost:4000/graphql'

graphql_request = GraphQLRequest(url)
df_dictionary = graphql_request.request()

dfs = list()
dfs_name = list()

# for name, data_frame in df_dictionary.items():
#     dfs.append(data_frame)
#     dfs_name.append(name)
# adding new line
# n = 0
# for i in dfs:
#     print(dfs_name[n])
#     n += 1
#     for j in i.columns[1:]:
#         a = list(i[j])
#         for o in a:
#             if o<0:
#                 print(a.index(o))


df_dictionary_copy = copy.deepcopy(df_dictionary)
clustering = Clustering(df_dictionary_copy)
clustered_df_dict = clustering.efficiency_rate_clustering()

corr = correlation.Correlation(lead_lag=4, currency_pair=['crude_oil', 'gold'],
                               currency_dict=copy.deepcopy(df_dictionary))
corr.correlation()

model = Model(clustered_df_dict)
model.train()
# for k, v in clustered_df_dict.items():
#     print(k)
#     print(v.tail())
