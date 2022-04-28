from graphqlrequest import GraphQLRequest
from clustering import Clustering
from prediction import Model
import correlation
import copy


'''Performing query with graphql to get historical data from mongodb as a dictionary'''
url = 'http://localhost:4000/graphql'
graphql_request = GraphQLRequest(url)
df_dictionary = graphql_request.request()

'''Clustering'''
df_dictionary_copy = copy.deepcopy(df_dictionary)
clustering = Clustering(df_dictionary_copy, plot=True)
clustered_df_dict = clustering.efficiency_rate_clustering()

'''Calculate and plot efficiency rate correlation between currency pairs with multi lead-lag'''
df_dictionary_copy = copy.deepcopy(df_dictionary)
corr = correlation.Correlation(lead_lag=4, currency_pair=['crude_oil', 'gold'],
                               currency_dict=df_dictionary_copy)
corr.correlation()

'''Train and evaluate a neural network for prediction'''
model = Model(clustered_df_dict)
model.train()
