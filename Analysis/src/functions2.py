import pandas 
import requests
import json
from dotenv import load_dotenv
import os
from pandas import json_normalize
import operator
from functools import reduce
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
load_dotenv()


def df_final(df1,df2,df3):
    df = pandas.concat([df1, df2, df3])
    df = df.drop(["alt", "elevation"], axis = 1) 
    df.reset_index(inplace = True)
    df.rename(columns={"standard": "city"}, inplace=True)

    df = df.drop(df[df["index"] == "addresst"].index)
    df = df.drop(df[df["index"] == "prov"].index)
    df = df.drop(df[df["index"] == "countryname"].index)
    df = df.drop(df[df["index"] == "postal"].index)
    df = df.drop(df[df["index"] == "loc"].index)
    df = df.drop(df[df["index"] == "confidence"].index)
    df = df.set_index('city')
    df = df.drop(["index"], axis = 1) 

    return df
    

def data(lat, lon):

    df = {}
    tok1 = os.getenv("token1")
    tok2 = os.getenv("token2")
    url_query = 'https://api.foursquare.com/v2/venues/explore'
    queries = ["Starbucks", "High School", "Middle School", "Preschool"]

    for i in queries: 
        parameters = {"client_id" : tok1,
                  "client_secret" : tok2,
                  "v": "20180323",
                  "ll": f"{lat}, {lon}",
                  "query":i,
                  "limit": 100,
                  "radius": 10000
        }  

        resp = json.loads(requests.get(url= url_query, params=parameters).text)       
        df[i] = resp
        
    return df
    

def clean(dic):

    for key, values in dic.items():
        
        if key == "Starbucks":
            Starbucks = dic.get(key)
            response = Starbucks.get('response')
            decoded = response.get('groups')[0]
            json_normalize(decoded)
            star = decoded.get('items')

        elif key == "High School":
            High = dic.get(key)
            response = High.get('response')
            decoded = response.get('groups')[0]
            json_normalize(decoded)
            hc = decoded.get('items')
            
            
        elif key == "Middle School":
            Middle = dic.get(key)
            response = Middle.get('response')
            decoded = response.get('groups')[0]
            json_normalize(decoded)
            mc= decoded.get('items')
            
        else:
            Pres = dic.get(key)
            response = Pres.get('response')
            decoded = response.get('groups')[0]
            json_normalize(decoded)
            pc = decoded.get('items')

            
    final = [star, hc,  mc, pc]
            
    return final



def getFromDict(diccionario,mapa):
    return reduce(operator.getitem,mapa,diccionario)

def to_df(*args):

    map_name = ["venue","name"]
    map_lat = ["venue","location","lat"]
    map_long = ["venue","location","lng"]
    map_cat = ["venue", "categories"]
    results = []

    for i in args:
        for dic in i:            
            paralista = {}
            paralista["name"] = getFromDict(dic,map_name)
            paralista["lat"] = getFromDict(dic,map_lat)
            paralista["long"] = getFromDict(dic,map_long)
            name = getFromDict(dic,map_cat)
            paralista["category"] = name[0]['name']
            results.append(paralista)
    df = pandas.DataFrame(results)

    return df

def mapping(df, lattitude, longitude): 

    map_ = Map(location=[lattitude,longitude],zoom_start=15)

    for i, row in df.iterrows():
        name = {
        "location":[row["lat"], row["long"]],
        "tooltip" : row["name"]
        }
    
        if row["category"] == "Coffee Shop":
            icon = Icon(color = "green",
                        prefix = "fa",
                        icon = "coffee",
                        icon_color = "black"
            )

        elif row["category"] == "Cafeteria":
            icon = Icon(color = "green",
                        prefix = "fa",
                        icon = "coffee",
                        icon_color = "black"
            )

        elif row["category"] == "High School":
            icon = Icon(color = "darkblue",
                        prefix = "fa",
                        icon = "graduation-cap",
                        icon_color = "black"
            )

        elif row["category"] == "Middle School":
            icon = Icon(color = "blue",
                        prefix = "fa",
                        icon = "flag",
                        icon_color = "black"
            )
            
        else:
            icon = Icon(color = "lightblue",
                        prefix = "fa",
                        icon = "flag-o",
                        icon_color = "black"
            )
        Marker(**name,icon = icon ).add_to(map_)
    return map_