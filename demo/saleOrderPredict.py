# 销售预测

# coding:utf-8# 用ARMA进行时间序列预测
import pandas as pd
#import matplotlib.pyplot as plt

df = pd.read_csv('D:\precast_sale.csv',parse_dates=['date'],index_col='date')
df['amount']= df['amount']/1000
#print(df)

# 季节性时间序列的可视化
df.reset_index(inplace=True)

#Prepare data
df['year'] = [d.year for d in df.date]
df['month'] = [d.strftime('%m') for d in df.date]
years = df['year'].unique()
grouped2 = df['amount'].groupby([df['year'],df['month']]).sum().reset_index()
#print(grouped2.loc[grouped2.year==2015,:])
#print(grouped2)

from pyecharts.faker import Faker

print(Faker.values())

print(Faker.choose())