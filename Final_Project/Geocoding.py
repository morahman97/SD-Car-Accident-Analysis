import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
import json
import time
import googlemaps
import gmaps        
import gmaps.datasets

def getLatitudeLongitude(address):
    
    #gmaps.configure(api_key="AIzaSyAw6aj9M--mAl9Rx0vCGoiVN7otm7Kgkl8")
    mymaps = googlemaps.Client(key='AIzaSyAw6aj9M--mAl9Rx0vCGoiVN7otm7Kgkl8')
    geocode_result = mymaps.geocode(address)
    for item in geocode_result:
        return [item['geometry']['location']['lat'], item['geometry']['location']['lng']]
    
    #return geocode_result['results'][0]['geometry']['location']


def main():
    listA = []
    listA.append(getLatitudeLongitude("UCSD"))
    visualizeMap(listA)

def visualizeMap(latLongs):

    gmaps.configure(api_key='AIzaSyAw6aj9M--mAl9Rx0vCGoiVN7otm7Kgkl8')
    my_df = pd.DataFrame()
    my_df['locs'] = latLongs
    locations = gmaps.datasets.load_dataset(my_df)

