#%% Task 4.1 

#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='data/raw/transshipment_vessels_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#Print the contents of the headerLine
print(headerLineString)

#%% Task 4.2

#Split the headerLineString into a list of header items
headerItems = headerLineString.split(",")

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = headerItems.index('mmsi')
name_idx = headerItems.index('shipname')
fleet_idx = headerItems.index('fleet_name')

#Print the values
print(mmsi_idx,name_idx,fleet_idx)

#%% Task 4.3
#Create an empty dictionary
vesselDict = {}
#Iterate through all lines (except the header) in the data file:
for lineString in lineList[1:]:
#Split the data into values
    lineData = lineString.split(',')
#Extract the mmsi value from the list using the mmsi_idx value
    mmsi = lineData[0]
#Extract the fleet value
    fleet = lineData[4]
#Adds info to the vesselDict dictionary
    vesselDict[mmsi] = fleet

print(len(vesselDict))

#Task 4.4 
vesselID = '258799000'
value = vesselDict[vesselID]
print(f"Vessel # {vesselID} flies the flag of {value}")

# Task 5
FileObj = open(file='data/raw/loitering_events_20180723.csv',mode='r')

LineList = FileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
FileObj.close() #Close the file

for LineString in LineList[1:]: 
    LineData = LineString.split(',')

    transshipment = LineData[0]
    start_lat = LineData[1]
    end_lat = LineData[3]
    start_long = LineData[2]
    end_long = LineData[4]

for key in keys: 
  start_lat < 0
  end_lat >0
  start_long > 165
  end_long < 175
  print(f"Vessel # {vesselID} flies the flag of {value}")



    if start_lat < 0 and end_lat > 0 and start_long > 165 and start_long < 170:
        shipment = LineData[0]
        if len(shipment) == 0:
            print("No vessels met the criteria")
        print(f"Vessel # {vesselID} flies the flag of {value}")
        


#keys = []

#for key, value in .items():
 # if value == user_date:
 #   keys.append(key)

#report if no records are found 
#if len(value) == 0:
 # print("No vessels met the criteria")

#Loop through keys and report locations 
#for key in keys: 
  #start_lat < 0
  #end_lat >0
  #start_long > 165
  #end_long < 175
  #print(f"Vessel # {vesselID} flies the flag of {value}")