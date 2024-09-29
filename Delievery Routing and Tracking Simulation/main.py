from truck import Truck
from package import Package
from hashtable import ChainingHashTable
from datetime import datetime, time, timedelta


import csv

# csv file names
packageFile = "WGUPS Package File.csv"
distanceFile = "WGUPS Distance Table.csv"
addressFile = "addresses.csv"

# initializing hast table
packageHash = ChainingHashTable()

# reading csv file
with open(packageFile, 'r', encoding='utf-8-sig') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting each data row one by one
    for row in csvreader:
        key = int(row[0])
        package_id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip_code = row[4]
        delivery_time = row[5]
        weight = row[6]
        status = 'At HUB'
        notes = row[7]
        newPackage = Package(package_id, address, city, state, zip_code, delivery_time, weight, status, notes)
        packageHash.insert(key, newPackage)



with open(addressFile,'r',encoding='utf-8-sig') as csvfile:
    addressRef = csv.reader(csvfile)
    key = []
    address = []
    for row in addressRef:
        if row:
            key.append(row[0])
            address.append(row[1].strip())


print(packageHash.search(6))

# Loading packages into trucks manually
# Packages 6,25,28,32 are delayed and not arriving until 9:05am 
truck1 = Truck("Truck 1", # Package 14 must be delivered with 15,19 and Package 20 must be delivered with 13,15
                  [1,2,13,14,15,19,20,21,27,29,30,33,34,35,37],
                  datetime(2024, 8, 23,8,0))

truck2 = Truck("Truck 2", # Packages 36,38,18,3 can only be on truck 2
                  [4,6,11,12,17,18,17,18,23,24,31,32,36,40,3,38],
                  datetime(2024,8,23,9,5))

truck3 = Truck("Truck 3",# Package 16 must be delivered with 13,19
                    [5,7,8,9,10,16,26,28,39,25,22],
                    datetime(2024,8,23,9,50)) # placeholder - truck 3 needs to wait until truck 1 returns

print(truck1)

#totalDistance = 0
#		currentLocation = Packages[hub]
#		while totalPackages > 0
#			nextLocation = packages[1]
#				For i in packages
#					if package[i].distance - currentLocation.distance < nextLocationDistance
#					nextLocationDistance = package[i].distance - currentLocation.distance
#					nextLocation = packages[I]
#					package.drop[nextLocation]
#				totalDistance = totalDistance + nextlocation.distance[0]

with open(distanceFile, 'r', encoding='utf-8-sig') as csvfile:
    distanceRef = csv.reader(csvfile)
    distanceRef = list(distanceRef)

def findDistance(row, column):
    distance = distanceRef[row][column]
    return float(distance)

print(findDistance(2,1))

# choosing the package closest to the location that the truck is currently at (greedy method)
def nearestLocation(start, package_list):
    smallest_distance = float('inf')
    next_location = None
    start_key = address_to_key(start)
    for package in package_list:
        id_to_key = address_to_key(package)
        if id_to_key is not None:
            distance = location_distances(start_key, id_to_key)
            if distance < smallest_distance:
                smallest_distance = distance
                next_location = package
    return next_location
