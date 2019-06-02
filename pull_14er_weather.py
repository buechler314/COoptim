
import urllib
import json
import numpy as np

import matplotlib.pyplot as plt
import datetime
import pandas
import os
import glob
import matplotlib.dates
import copy

# ------------ Inputs ---------------------------------
location = 'Mt Massive'
parameters = 'temperature'

# lightningActivityLevel, probabilityOfPrecipitation, skyCover, snowLevel
# snowfallAmount, temperature, windChill, windSpeed, windGust, relativehumidity
# maxTemperature, minTemperature, iceAccumulation, apparentTemperature
# -----------------------------------------------------

def getInfo(whichOne,index):
    time=list()
    value=list()
    width = 0.5
    
    if index == 1:
        width = 7
        
    for i in parsed_json['properties'][whichOne]['values']:
        #time_T.append(i['validTime'])
        time_temp=datetime.datetime.strptime(i['validTime'][0:19],'%Y-%m-%dT%H:%M:%S')
        time.append(time_temp.strftime('%Y-%m-%d %H:%M:%S'))
        value.append(i['value'])
    
    value       =np.array(value)
    time        =np.array(time)
    value_df    =pandas.DataFrame(np.concatenate((time.reshape(-1,1),value.reshape(-1,1)),axis=1),columns=['time',whichOne])
    ax          =plt.gca()
    ax.plot_date(pandas.DatetimeIndex(value_df['time']),np.array(value),'.-',color='C'+str(j%10),linewidth=width)
    
   
    return(ax)
    
#%% load data

#os.chdir('C:\\Users\Lily Buechler\Desktop\\14ers')
coord=pandas.read_csv('C:/Users/Owner/Desktop/COstuff/trailhead_coord.csv',names=['trailhead','lat','long'])

## --------------get request list

index = 0
count = -1
url_list=[]

for index in range(len(coord.trailhead)):
    f = urllib.request.urlopen('https://api.weather.gov/points/'+str(coord.lat[index])+','+str(coord.long[index]))     
    
    json_string = f.read()
    parsed_json = json.loads(json_string)
    f.close()
    
    #print(parsed_json['properties']['forecastGridData'])
    if (parsed_json['properties']['forecastGridData'] in url_list)==False:
        url_list.append(parsed_json['properties']['forecastGridData'])
        count = count + 1

    if index == coord[coord['trailhead']==location].index.values.astype(int)[0]:
        rightOne = count
## --------------------- pull data

plt.figure(figsize=(30,20))
j=0
index = 0
for url in url_list:
    
    #print(url)
    f = urllib.request.urlopen(url)     
    json_string = f.read()
    parsed_json = json.loads(json_string)
    f.close()
    
    if j == rightOne:
        index = 1
        
    ax = getInfo(parameters,index)
    index = 0
    j=j+1

labelSize = 35
formatter = matplotlib.dates.DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=30, labelsize=labelSize)
ax.tick_params(axis='both', which='major', labelsize=labelSize)

plt.ylabel(parameters + ', ' + parsed_json['properties'][parameters]['uom'],fontsize=labelSize)
plt.grid(True)
