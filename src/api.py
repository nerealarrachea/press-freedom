

import pandas as pd 
import requests

def worldbank(name, code):
    url = 'http://api.worldbank.org/v2/country/all/indicator/{}?format=json&date=2020&per_page=6000'
    response = requests.get(url.format(code))
    data = response.json()
    df = pd.json_normalize(data[1])
    df = df[['country.id','country.value', 'date', 'value']]
    df.columns = ['Country code', 'Country', 'Year', name]
    return df

