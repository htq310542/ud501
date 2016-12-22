import pandas as pd
import matplotlib.pyplot as plt
import unittest
import numpy as np

class UdaCity_MLT(unittest.TestCase):

    def test_run(self):
        df = pd.read_csv("data/aapl.csv")
        df[['Adj Close', 'Close']].plot()
        plt.show()

    def test_run2(self):
        start_date='2016-12-01'
        end_date='2016-12-15'
        dates=pd.date_range(start_date,end_date)
        df1=pd.DataFrame(index=dates)
        #print(df1)

        #read SPY data
        ds_spy = pd.read_csv('data/spy.csv', index_col='Date',
                             parse_dates=True, usecols=['Date', 'Adj Close'],
                             na_values=['nan'])

        #print(ds_spy)
        df1=df1.join(ds_spy, how='inner') #left, right, inner, outer
        #df1 = df1.dropna()
        df1.plot()
        plt.show()

    def test_np(self):
        a = np.random.randint(0,500,10)
        print('for a = {} max(a)=a[{}]={}'.format(a, a.argmax(), a.max()))
        print('a.size={}'.format(a.size))
        print('a slice [:5] = {}'.format(a[:5]))

    