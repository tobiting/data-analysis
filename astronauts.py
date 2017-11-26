"""
Reading in and printing the name of the astronauts currently on ISS
"""

import pandas as pd
import requests

response = requests.get("http://api.open-notify.org/astros.json")   # request to get astronauts

data = response.json()                                              # convert the response to json

df = pd.DataFrame(data)                                             # make a dataframe from the data

for i in range(len(df["people"])):
    print df["people"][i]["name"]


