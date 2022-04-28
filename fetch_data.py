from yahoofinancials import YahooFinancials
from datetime import date
import pandas as pd
import datetime
import requests
import pymongo
import json

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['currency_pairs']

"""Fetch Crude Oil Historical Data From Yahoo Finance."""

curr_list = ['CL=F', 'GC=F']
curr_name = ['crude_oil', 'gold']

col_list = db.list_collection_names()

if 'crude_oil' in col_list:
    my_col = db["crude_oil"]
    my_col.drop()

if 'bitcoin' in col_list:
    my_col = db["bitcoin"]
    my_col.drop()

if 'gold' in col_list:
    my_col = db["gold"]
    my_col.drop()

"""Collecting Yahoo Finance Data Into The MongoDB"""

for cr in range(len(curr_list)):

    """Yahoo Finance API."""
    yahoo_financials = YahooFinancials(curr_list[cr])
    data = yahoo_financials.get_historical_price_data(start_date='2017-08-17',
                                                      end_date=str(datetime.datetime.now().date()),
                                                      time_interval='daily')
    currency_df = pd.DataFrame(data[curr_list[cr]]['prices'])
    cur_col = db[curr_name[cr]]

    """Putting Data To MongoDB."""
    for i in range(currency_df.shape[0]):
        cur_col.insert_one({"date": str(date.fromisoformat(currency_df.iloc[i][-1])),
                            "high": str(currency_df.iloc[i][1]),
                            "low": str(currency_df.iloc[i][2]),
                            "open": str(currency_df.iloc[i][3]),
                            "close": str(currency_df.iloc[i][4]),
                            "volume": str(currency_df.iloc[i][5]),
                            })

"""Collecting Binance Data To MongoDB"""

url = 'https://api.binance.com/api/v3/klines'
symbol = 'BTCUSDT'
interval = '1d'

last_day = datetime.datetime(2017, 8, 17).date()
today = datetime.datetime.today().date()
next_to_last_day_timestamp = datetime.datetime(2017, 8, 17).timestamp()
f = 0
try:
    while today != last_day:
        start = str(int(next_to_last_day_timestamp * 1000))
        end = str(int(datetime.datetime.today().timestamp() * 1000))

        par = {'symbol': symbol, 'interval': interval, 'startTime': start, 'endTime': end}
        btc_df = pd.DataFrame(json.loads(requests.get(url, params=par).text))
        # format columns name
        btc_df.columns = ['datetime', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'qav', 'num_trades',
                          'taker_base_vol', 'taker_quote_vol', 'ignore']
        btc_df.index = [datetime.datetime.fromtimestamp(x / 1000.0) for x in btc_df.datetime]
        btc_df = btc_df.astype(float)

        cur_col = db['bitcoin']

        """Putting Data To MongoDB."""
        for i in range(btc_df.shape[0]):
            cur_col.insert_one({"date": str(btc_df.index[i].date()),
                                "high": str(btc_df.iloc[i][2]),
                                "low": str(btc_df.iloc[i][3]),
                                "open": str(btc_df.iloc[i][1]),
                                "close": str(btc_df.iloc[i][4]),
                                "volume": str(btc_df.iloc[i][5]),
                                })

        my_doc = cur_col.find({}, {'date': 1, '_id': -1}).sort("_id", -1).limit(1)

        year = int(my_doc[0]['date'][0:4])
        month = int(my_doc[0]['date'][5:7])
        day = int(my_doc[0]['date'][8:10])
        last_day = datetime.datetime(year, month, day).date()
        today = datetime.datetime.today().date()
        next_to_last_day_timestamp = datetime.datetime(year, month, day).timestamp() + 86400.0

except:
    f = 1
    pass

if f == 1:
    print("There is some problem with fetching bitcoin data.")
    print("Make sure that your vpn is on.")

else:
    print("Data is ready.")
