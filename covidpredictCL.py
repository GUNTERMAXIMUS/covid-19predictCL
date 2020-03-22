try:
  %tensorflow_version 2.x
  import tensorflow as tf
  from tensorflow import keras
except OSError:
  print(tf.__version__)
finally:
  import numpy as np
  import pandas as pd
  import matplotlib.pyplot as plt
  print(tf.__version__)
  import requests as rq
  import io
#  from google.colab import drive
#  drive.mount('/content/gdrive', force_remount = True, timeout_ms = 60000)

 ###

url = 'https://raw.githubusercontent.com/GUNTERMAXIMUS/covid-19predictCL/master/covid_19_data.csv'
respond = rq.get(url).content

df_data = pd.read_csv(io.StringIO(respond.decode('utf-8')), 
                      sep = ',', 
                      quotechar = '"', 
                      usecols = [1, 3, 5, 6 , 7], 
                      encoding = 'utf-8')

###

x = df.ObservationDate

plt.figure(figsize = (10, 6))
plt.bar(x, (df.Confirmed)-(df.Recovered + df.Deaths), label = 'Confirmed', color = 'blue')
plt.bar(x, df.Recovered, label = 'Recovered', color = 'green')
plt.bar(x, df.Deaths, label = 'Deaths', color = 'red')
plt.stackplot(x, df.Confirmed, df.Recovered, df.Deaths)
plt.xlabel('amount')
plt.ylabel('time sequences')
plt.legend(loc = 'upper left')
plt.xticks(rotation = 'vertical')
plt.tight_layout()
plt.grid(True)

plt.show()

###
