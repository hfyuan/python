#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import pandas as pd 
import numpy as np
from datetime import datetime

S1 = pd.Series()
print(S1)

S2 = pd.Series([1,3,5,7,9],\
    index=['a','b','c','d','e'])
print(S2)

print(S2.values)
print(S2.index)

S2['f']=11

print(S2.values)
print(S2.index)

S3= pd.Series([1,3,-4,-7])
print(S3)

np.random.seed(8888)
S4= pd.Series(np.random.randn(5))
print(S4)

S4= pd.Series(np.arange(2,9))
print(S4)

S4 = pd.Series([0,np.NaN, 2,4,6,8,True,10,12])

print(S4.head(3))

print(S4.tail(4))

print(S4.take([2,3,7]))

print(S2[[1,3,5]])

date = datetime(2019,1,1)
date = pd.Timestamp(date)
print(date)

print(type(date))

ts = pd.Series(1,index=[date])
print(ts)

print(ts.index)

dates=['2016-1-1', '2017-1-1', '2018-1-1']

ts = pd.Series([1,2,3], index = pd.to_datetime(dates))

print(ts)
ts.shift(1)
print(ts.truncate(after='2017-1-2'))


ts.shift(-1)
print(ts.truncate(after='2017-1-2'))




dates=['2016-01-01', '2016-01-02', '2016-01-03',\
    '2016-01-04', '2016-01-05', '2016-01-06']
print(dates)
df = pd.DataFrame(np.random.randn(6,4), index = dates, columns=list('ABCD'))

print(df)
'''
headerlist = list('longitude','latitude','housing_median_age','total_rooms',\
    'total_bedrooms','population','households','median_income',\
        'median_house_value','ocean_proximity') 
'''
df1 = pd.read_csv('datasets/housing/housing.csv',header=None, sep=',')

print(df)



print(df.columns)
print(df.index)
print(df.values)
print(df.describe())
#print(df1['1'])
print(df[1:3])
print(df[['A','C']])

print(df[df['A']>0])

print(df.loc[dates[0],'A'])

print(df.iloc[2])
print(df.iloc[:,2])

print(df)
print(df.iloc[[1,2,4],[1,3]])