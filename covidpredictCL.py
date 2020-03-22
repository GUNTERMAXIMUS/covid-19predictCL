import tensorflow as tf
from tensorflow import keras

try:
  %tensorflow_version 2.x
except OSError:
  print(tf.__version__)
finally:
  import numpy as np
  import pandas as pd
  import matplotlib.pyplot as plt
  print(tf.__version__)
  from google.colab import drive
  drive.mount('/content/gdrive', force_remount = True, timeout_ms = 60000)

 ###

 file_path = 'gdrive/My Drive/Colab Notebooks/'
 f_data = file_path + 'covid_19_data.csv' 
 df_data = pd.read_csv(f_data, 
                       sep = ',', 
                       quotechar = '"', 
                       usecols = [1, 3, 5, 6 , 7], 
                       encoding = 'utf-8')

df = df_data[df_data['Country/Region'].str.contains('Chile')]
print(df.isnull().any())
df.head(10)

###

x = df.ObservationDate

plt.figure(figsize = (10, 6))
plt.bar(y, (df.Confirmed)-(df.Recovered + df.Deaths), label = 'Confirmed', color = 'blue')
plt.bar(y, df.Recovered, label = 'Recovered', color = 'green')
plt.bar(y, df.Deaths, label = 'Deaths', color = 'red')
plt.stackplot(y, df.Confirmed, df.Recovered)
plt.xlabel('amount')
plt.ylabel('time sequences')
plt.legend(loc = 'upper left')
plt.xticks(rotation = 'vertical')
plt.tight_layout()
plt.grid(True)

plt.show()

###

