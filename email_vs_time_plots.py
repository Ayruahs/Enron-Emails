import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = 'emails.csv'
#dataset = pd.read_csv(filename, nrows=10000)
dataset = pd.read_csv(filename)

print(dataset.shape)

def returnDate(email):
    message = email.split('\n')
    date = message[1][5:]
    return date
    
messages = dataset['message']

stringDates = []
for message in messages:
    date = returnDate(message)
    stringDates.append(date)
    
dates = pd.to_datetime(stringDates, infer_datetime_format=True)

dataset['year'] = pd.Series(dates.year)
dataset['month'] = pd.Series(dates.month)
dataset['week'] = pd.Series(dates.week)
dataset['day'] = pd.Series(dates.dayofweek)
print(dataset.groupby('year').count())

fig = dataset.groupby('day').count().plot()
#plt.xlim([1980,2040])
#plt.ylim([0,300000])
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
fig.set_xticklabels(days)
fig.set_xlabel('Day of week')
fig.set_ylabel('Number of emails')

plt.grid()
plt.show()