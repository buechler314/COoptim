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
import functools
import subprocess

def costFunction(x,lower,upper,costType):
    conds = [x <= lower, (x > lower) & (x < upper), x >= upper]
    if costType == 'linear':
        funcs = [lambda x: -1*(x-lower)+0, 
                 0, 
                 lambda x: 1*(x-upper)+0]
    if costType == 'quad':
        funcs = [lambda x: (x-lower)**2, 
                 0, 
                 lambda x: (x-upper)**2]   
    cost = np.piecewise(x, conds, funcs)
    return cost

def mapValue(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = np.array(value - leftMin) / np.array(leftSpan)
    return rightMin + (valueScaled * rightSpan)

# --------------------------------------------------------------------------------------------------------------
# ------------ Inputs ------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
currentLocation = 'NA'              # 'NA' if you don't want to consider distance
parameters = ['probabilityOfPrecipitation','skyCover','windSpeed','temperature','lightningActivityLevel']
parameterWeights = [0.8, 0.6, 0.5, 0.5, 1]
distanceWeight = 0.6
parameterLower = [0,0,0,5,0]                    # lower bound for "tolerable": temp in C, wind in m/s, lightning 1-6
parameterUpper = [20,30,5,15,2]                 # Upper bound for "tolerable"
parameterNormLower = [0,0,0,-10,0]               # Lower bound for normalization
parameterNormUpper = [100,100,40,32,6]          # Upper bound for normalization
costType = 'quad'                               # linear or quad
filePath = 'C:/Users/Owner/Desktop/COstuff/'
openMATLAB = 0          # 1 or 0 (yes or no)
knownURLs = 0           # 1 or 0 (yes or no)
plotCostEquations = 0   # 1 or 0 (yes or no)

# ------------ Change Lines ------------
# Python: 36,213,228,230
# MATLAB: none

# ------------ Important Variables ------------
# DataByTrailhead   - All time-synced numerical cost data organzed by trailhead
# csvData           - A single matrix containing cost data for all times for all trailheads
# sortedRiskOrder   - Contains order of max to min risk score for each time slot

# ------------ possible parameters ------------
# lightningActivityLevel, probabilityOfPrecipitation, skyCover, snowLevel
# snowfallAmount, temperature, windChill, windSpeed, windGust, relativehumidity
# maxTemperature, minTemperature, iceAccumulation, apparentTemperature
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
    
# Load trailhead data from csv file
coord=pandas.read_csv(filePath+'trailhead_coord.csv',names=['trailhead','lat','long'])

if currentLocation != 'NA':
    distancesTemp = pandas.read_csv(filePath+'MountainData.csv')
    distancesTemp['FROM mtn ID#'] = distancesTemp['FROM mtn ID#']-1
    distancesTemp['TO mtn ID#'] = distancesTemp['TO mtn ID#']-1
    mountainID = int(coord.loc[coord['trailhead'] == currentLocation].index.values)
    distances = distancesTemp[(distancesTemp['FROM mtn ID#'] == mountainID) | (distancesTemp['TO mtn ID#'] == mountainID)]
                                   
# Get URLS for each trailhead coordinate
index = 0
url_list=[]
if knownURLs == 0:
    for index in range(len(coord.trailhead)):
        print('Getting URLs: %.1f percent' % float((np.float(index)/np.float(len(coord.trailhead)))*100))
        f = urllib.request.urlopen('https://api.weather.gov/points/'+str(coord.lat[index])+','+str(coord.long[index]))     
        json_string = f.read()
        parsed_json = json.loads(json_string)
        f.close()
        url_list.append(parsed_json['properties']['forecastGridData'])
    # Write URL list to file for future use
    print('Writing URLs to file')
    with open('URLlist.txt', 'w') as filehandle:  
        for listitem in url_list:
            filehandle.write('%s\n' % listitem)

if knownURLs == 1:
    print('Getting URLs: 0 percent')
    with open('URLlist.txt', 'r') as filehandle:  
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]
            # add item to the list
            url_list.append(currentPlace)
    print('Getting URLs: 100 percent')
coord['URL'] = url_list   

# Get Data
parameterSpecs = dict.fromkeys(parameters)
count = 0
DataByTrailhead = dict.fromkeys(coord['trailhead'])
merged = dict.fromkeys(parameters)
interpolated = dict.fromkeys(parameters)

for parameter in parameters:
    parameterSpecs[parameter] = {}
    parameterSpecs[parameter]['Weight'] = parameterWeights[count]
    parameterSpecs[parameter]['Lower'] = parameterLower[count]
    parameterSpecs[parameter]['Upper'] = parameterUpper[count]
    parameterSpecs[parameter]['NormUpper'] = parameterNormUpper[count]
    parameterSpecs[parameter]['NormLower'] = parameterNormLower[count]
    count = count + 1

# Save certain data points
j=0
columns = ['time']
for trailhead in coord['trailhead']:
    url = coord['URL'][j]
    DataByTrailhead[trailhead] = {}
    
    # Get all data for that one location
    f = urllib.request.urlopen(url)     
    json_string = f.read()
    parsed_json = json.loads(json_string)
    f.close()
       
    # save data from certain parameters  
    for parameter in parameters:
        time=list()
        value=list()
            
        for i in parsed_json['properties'][parameter]['values']:
            time_temp=datetime.datetime.strptime(i['validTime'][0:19],'%Y-%m-%dT%H:%M:%S')
            time.append(time_temp.strftime('%Y-%m-%d %H:%M:%S'))
            value.append(i['value'])
        
        value       =np.array(value)
        time        =np.array(time)
        value_df    =pandas.DataFrame(np.concatenate((time.reshape(-1,1),value.reshape(-1,1)),axis=1),columns=['time',parameter])
        
        DataByTrailhead[trailhead][parameter] = {}
        DataByTrailhead[trailhead][parameter] = value_df
        
        if j==0:
            merged[parameter]=value_df
        
        if j>0:
            merged[parameter] = pandas.merge(merged[parameter],value_df, sort=True, on='time', how='outer')
    
    print('Retrieved forcast - ' + trailhead)           
    j=j+1
    
# Rename Columns of merged data, convert to numeric, and interpolate between trailheads
datesList = list()
for parameter in parameters:
    merged[parameter] = merged[parameter].set_index('time')
    merged[parameter].columns = list(coord['trailhead'])
    merged[parameter] = merged[parameter].apply(pandas.to_numeric)
    interpolated[parameter] = merged[parameter].interpolate(method ='linear', limit_direction ='both') 
    interpolated[parameter].index = pandas.DatetimeIndex(interpolated[parameter].index.values)
    datesList.append(interpolated[parameter].index[-1])

furthest=min(datesList)
print('Final Time: '+str(furthest))

# Interpolating between weather parameters
j = 0
for trailhead in coord['trailhead']:
    i = 0
    for parameter in parameters:
        print('Interpolating '+parameter+' for ' + trailhead)
        if i == 0:
            temp2 = pandas.DataFrame()
            temp = interpolated[parameter].reset_index()
            temp2['index'] = temp['index']
            temp2[parameter] = temp[trailhead]
            DataByTrailhead[trailhead]['TimeData'] = temp2[temp['index'] < furthest]
        if i > 0:
            temp = interpolated[parameter].reset_index()
            temp2 = pandas.DataFrame()
            temp2['index'] = temp['index']
            temp2[parameter] = temp[trailhead]
            DataByTrailhead[trailhead]['TimeData'] = pandas.merge(DataByTrailhead[trailhead]['TimeData'],temp2[temp['index'] < furthest], sort=True, on='index', how='outer')
        i = i+1
        
    j = j+1  
    
    # interpolate
    DataByTrailhead[trailhead]['TimeDataInter'] = DataByTrailhead[trailhead]['TimeData'].interpolate(method ='linear', limit_direction ='both')
      
    # adjust for time zone
    DataByTrailhead[trailhead]['TimeDataInter']['index'] -= datetime.timedelta(hours=6)
     
# Calculating costs and plotting
plt.figure(figsize=(25,15))
ax=plt.gca()
j = 0
distanceCost = 0
csvData = pandas.DataFrame(index=DataByTrailhead[next(iter(DataByTrailhead))]['TimeDataInter']['index'])

for trailhead in coord['trailhead']:
    print('Calculating risk for '+ trailhead)
    DataByTrailhead[trailhead]['Cost']=pandas.DataFrame()
            
    for parameter in parameters:
        #costFunction(x,lower,upper,costType)
        #mapValue(value, leftMin, leftMax, rightMin, rightMax)
        mappedValues = mapValue(DataByTrailhead[trailhead]['TimeDataInter'][parameter].values,parameterSpecs[parameter]['NormLower'],parameterSpecs[parameter]['NormUpper'],0,1)
        mappedLowerTol = mapValue(parameterSpecs[parameter]['Lower'],parameterSpecs[parameter]['NormLower'],parameterSpecs[parameter]['NormUpper'],0,1)
        mappedHigherTol = mapValue(parameterSpecs[parameter]['Upper'],parameterSpecs[parameter]['NormLower'],parameterSpecs[parameter]['NormUpper'],0,1)
        DataByTrailhead[trailhead]['Cost'][parameter] = costFunction(mappedValues,mappedLowerTol,mappedHigherTol,costType) * parameterSpecs[parameter]['Weight']
    DataByTrailhead[trailhead]['Cost'].index = DataByTrailhead[trailhead]['TimeDataInter']['index'] 
    
    # compute travel time in seconds 
    if currentLocation != 'NA':
        if trailhead != currentLocation:
            # travel time in minutes
            addition = float((1/60) * (distances[(distances['FROM mtn ID#'] == int(coord.loc[coord['trailhead'] == trailhead].index.values)) | (distances['TO mtn ID#'] == int(coord.loc[coord['trailhead'] == trailhead].index.values))]['Travel duration [s]']))
            # mapped distance in minutes
            mappedAddition = mapValue(addition,0,max(distances['Travel duration [s]']),0,1)
            distanceCost = mappedAddition*distanceWeight          
        if trailhead == currentLocation:
            distanceCost = 0
        
    DataByTrailhead[trailhead]['Cost']['Distance'] = distanceCost
    DataByTrailhead[trailhead]['Cost']['Cost'] = DataByTrailhead[trailhead]['Cost'].sum(axis=1)
    
    ax.plot_date(pandas.DatetimeIndex(DataByTrailhead[trailhead]['Cost'].index.values),np.array(DataByTrailhead[trailhead]['Cost']['Cost']),'.-',color='C'+str(j%10),linewidth=1)
    csvData[trailhead] = np.array(DataByTrailhead[trailhead]['Cost']['Cost'])
    j = j + 1
    
labelSize = 20
formatter = matplotlib.dates.DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=30, labelsize=labelSize)
ax.tick_params(axis='both', which='major', labelsize=labelSize)
plt.ylabel('Risk Level',fontsize=labelSize)
plt.grid(True)

# Write data to csv
print('Writing to CSV')
csvData.to_csv(r'C:\Users\Owner\Desktop\COstuff\RiskData.csv')

# Print out name of best trailhead for each time slot
#print(csvData.idxmin(axis=1))

# Sort out trailheads (max to min risk score) for each time slot
temp = np.flip(csvData.values.argsort(),1)
sortedRiskOrder = pandas.DataFrame(csvData.columns[temp], index=csvData.index)
#print(sortedRiskOrder)

# Show cost plot
#plt.show()

############### plotting cost function for all parameters, every trailhead, every time  #############
############### can copy paste entire for loop in command window after file has run     #############
if plotCostEquations == 1:
    for parameter in parameters:
        costType = 'quad'
        labelSize = 30
        
        xx = np.linspace(0, 1, 100)
        plt.figure(figsize=(20,15))
        matplotlib.rc('xtick', labelsize=labelSize) 
        matplotlib.rc('ytick', labelsize=labelSize) 
        
        lower = mapValue(parameterSpecs[parameter]['Lower'],parameterSpecs[parameter]['NormLower'],parameterSpecs[parameter]['NormUpper'],0,1)
        upper = mapValue(parameterSpecs[parameter]['Upper'],parameterSpecs[parameter]['NormLower'],parameterSpecs[parameter]['NormUpper'],0,1)
        
        for x in range(DataByTrailhead[trailhead]['TimeDataInter'][parameter].shape[0]):
            plt.plot(xx, costFunction(xx,lower,upper,costType))
            for trailhead in coord['trailhead']:
                mappedValues = mapValue(DataByTrailhead[trailhead]['TimeDataInter'][parameter].values,parameterSpecs[parameter]['NormLower'],parameterSpecs[parameter]['NormUpper'],0,1)
                plt.axvline(x=mappedValues[x])
        #    for value in mappedValues:
        #        plt.axvline(x=value)
            
        plt.xlabel('Normalized '+parameter,fontsize=labelSize)
        plt.ylabel(parameter+' Cost before weight',fontsize=labelSize)
        plt.show() 

############## send command to command prompt to run matlab script
if openMATLAB == 1:
    MATLABpath = '\"C:\\Program Files\\MATLAB\\R2018b\\bin\\matlab.exe\"'
    string2 = ' -nodisplay -nosplash -nodesktop -r \"'
    string3 = "run('C:\\Users\\Owner\\Desktop\\COstuff\\RiskData.m');\""
    string = MATLABpath+string2+string3
    subprocess.run(string)





############# Sample plot of one parameter at one location #############
#trailhead = 'North Elbert'
#parameter = 'temperature'
#plt.figure(figsize=(20,15))
#ax          =plt.gca()
#ax.plot_date(pandas.DatetimeIndex(DataByTrailhead[trailhead]['TimeDataInter']['index']),np.array(DataByTrailhead[trailhead]['TimeDataInter'][parameter]),'.-',color='C'+str(j%10),linewidth=1)
#labelSize = 20
#ax.xaxis.set_tick_params(rotation=30, labelsize=labelSize)
#ax.tick_params(axis='both', which='major', labelsize=labelSize)
#plt.grid(True)
#plt.show()







