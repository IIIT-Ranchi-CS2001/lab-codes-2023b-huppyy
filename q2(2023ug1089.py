import pandas as pd


data = pd.read_csv('AQI_Data.csv')


result = {}
for city, group in data.groupby('City'):
    avg_aqi = group['AQI'].mean()
    max_pm25 = group['PM2.5'].max()
    min_pm10 = group['PM10'].min()
    result[city] = [avg_aqi, max_pm25, min_pm10]


print(result)
