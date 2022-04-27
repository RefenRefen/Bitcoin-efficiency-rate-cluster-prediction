import pandas as pd
import requests
import json


query = '''query {
    %s {
        date
        high
        low
        open
        volume
        close
}
}'''

queries = list()
query_list = ['golds', 'bitcoins', 'crudeOils']

for currency in query_list:
    q = query % currency
    queries.append(q)


class GraphQLRequest:
    def __init__(self, url):
        self.url = url

    def request(self):
        self.url += '?query={q}'
        df_name = ['gold', 'bitcoin', 'crude_oil']
        df_dictionary = dict()

        for k in range(len(queries)):
            file = requests.get(self.url.format(q=queries[k]))
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

        return df_dictionary
