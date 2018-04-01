
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import pandas as pd

import matplotlib.dates as mdates


# Construct list of indices as put forward by EIOPA (Consultation Paper 14/058 of June 30th, 2015) - ex-Poland (as Yahoo Finance does not offer this index)

indices = ['FTSEMIB.MI', '^GDAXI', '^FCHI', '^FTAS', '^IBEX', '^AEX', '^N225', '^OMX', '^GSPC', '^SSMI']

# Source data from Yahoo Finance & save to csv

data = web.DataReader(indices, data_source='yahoo', start='01/01/2005')['Adj Close']
data.to_csv("Data.csv", sep=';', encoding='utf-8')

# or alternatively load the source data included in this repository

data_set = pd.read_csv('Data.csv', sep=';')

# set dates as the index, fill NaNs with previous values, drop the first line in the DF as it solely contains NANs

data_set.set_index('Date', inplace=True)
data_set.sort_index(inplace=True, ascending=True)
data_set.index = pd.to_datetime(data_set.index)

data_set.fillna(method='ffill', inplace=True)
data_set.drop(data_set.index[:1], inplace=True)

print(data_set.head())

# weight the closing prices of each index to get a global index (see EIOPA consultation)

data_set["^GDAXI"] *= float(0.22)
data_set["^FCHI"] *= float(0.14)
data_set["^FTAS"] *= float(0.14)
data_set["^AEX"] *= float(0.14)
data_set["^IBEX"] *= float(0.08)
data_set["FTSEMIB.MI"] *= float(0.08)
data_set["^OMX"] *= float(0.08)
data_set["^GSPC"] *= float(0.08)
data_set["^N225"] *= float(0.02)
data_set["^SSMI"] *= float(0.02)

# construct global index and calculate rolling 3-year moving average

data_set['global_index'] = data_set.sum(axis=1)
data_set['moving_average'] = data_set['global_index'].rolling(window=750).mean()

# calculate symmetric adjustment

data_set["symmetric_adjustment"] = (((data_set['global_index'] - data_set['moving_average']) / data_set['global_index'])- float(0.08))*float(0.5)

# calculate SCR

data_set["SCR"] = float(0.39)+data_set["symmetric_adjustment"]

# adjust SCRs below 0.29 and above 0.49 so that they reflect the lower, upper boundary

data_set['SCR'] = data_set['SCR'].apply(lambda x: 0.29 if x < 0.29 else x)
data_set['SCR'] = data_set['SCR'].apply(lambda x: 0.49 if x > 0.49 else x)

print(data_set.tail())

# plot SCR

plt.style.use('ggplot')

years = mdates.YearLocator()
yearsFmt = mdates.DateFormatter("'%y")

fig1 = plt.figure(figsize=(9,7))
ax1 = fig1.add_subplot(111)

ax1.plot(data_set.index, data_set["SCR"])
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(yearsFmt)
ax1.set_title("Equity Risk SCR", weight='bold')

# plot global index

fig2 = plt.figure(figsize=(9,7))
ax2 = fig2.add_subplot(111)

ax2.plot(data_set.index, data_set["global_index"])
ax2.xaxis.set_major_locator(years)
ax2.xaxis.set_major_formatter(yearsFmt)
ax2.set_title("Global Index (as stipulated by EIOPA)", weight='bold')

plt.show()





