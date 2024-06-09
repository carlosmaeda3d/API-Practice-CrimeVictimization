import pandas as pd
import requests
import matplotlib.pyplot as plt

def getData(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

# Using Personal Victimization API
api_url = 'https://data.ojp.usdoj.gov/resource/gcuy-rt5g.json?$query=select * where year in ("2020", "2021", "2022") limit 66000'
data = getData(api_url)

# Turn data into a dataframe
df = pd.DataFrame(data)

# Keep only selected index numbers. Can change this by index numbers in list
columnsToKeepList = [0, 2, 3, 4, 6, 11, 12, 13, 19, 20, 21, 22, 24, 26, 27, 28, 29, 31, 32]
selectedColumns = df.iloc[:, columnsToKeepList]
#print(list(selectedColumns.columns))

# Data split by years
data2020 = selectedColumns[selectedColumns['year'] == '2020']
data2021 = selectedColumns[selectedColumns['year'] == '2021']
data2022 = selectedColumns[selectedColumns['year'] == '2022']

print(data2021)

#Setup for matplotlib
plt.figure(figsize=(10,6))
