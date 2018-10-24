import time
from datetime import timedelta
from datetime import datetime as dt
import pandas as pd 
import requests
from darksky import forecast

'''
To convert isoformat() to normal date time()
time = datetime(2018, 10, 10).isoformat()
d = dateutil.parser.parse(time)
print(d)

# To print from normal date to isoformat()
d = datetime(2018,10,12)
date = d.isoformat()
print(date)

'''

key = '6913a13b7717b5b7a8a1b72efc77f1ee'
SLC = key, 40.765563, -111.869938
day = 7

data = []
def consecutive_dates(date, day):
    for i in range(day):
        date += timedelta(days=1)
        mod_dt = date.isoformat()
        # return mod_dt

        slc_data = forecast(*SLC, time=mod_dt)
        prediction_temp = [hour.temperature for hour in slc_data.hourly[:24]] # for a week worth data before 22nd Oct 2018
        data.append(prediction_temp)
        prediction_temp = sum(data, [])
        df_temp = pd.DataFrame(prediction_temp)
        return df_temp
    # print(df_temp)
    # print(d)

consecutive_dates(dt(2018,10,15), 7)
print(consecutive_dates)

# Converting into a data frame using pandas. Check this
# df_temp = pd.DataFrame(prediction_temp)
# print(df_temp)

# print("Current temperature is  ", slc_data.temperature)
# print("Temperature for following 24 hours is ", prediction_temp)

# humidity = slc_data.humidity
# prediction_humidity = [hour.humidity for hour in slc_data.hourly[:24]]
# df_humidity = pd.DataFrame(prediction_humidity)

#print("Current humidity is  ", humidity)
#print("Humidity for following 24 hours is ", prediction_humidity)

