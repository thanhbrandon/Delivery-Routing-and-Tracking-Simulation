# Student ID 011652606
from truck import Truck
from package import Package
from hashtable import ChainingHashTable
from datetime import datetime, time, timedelta

import csv

# csv file names
packageFile = "WGUPS Package File.csv"
distanceFile = "WGUPS Distance Table.csv"
addressFile = "addresses.csv"

# Initializing chaining hash table
packageHash = ChainingHashTable()

# Reading package data into hast table
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
        deadline = row[5]
        weight = row[6]
        status = 'At HUB'
        notes = row[7]
        newPackage = Package(package_id, address, city, state, zip_code, deadline, weight, status, notes)
        packageHash.insert(key, newPackage)


# Reading Address File into Key and Address lists
with open(addressFile,'r',encoding='utf-8-sig') as csvfile:
    addressRef = csv.reader(csvfile)
    key = []
    address = []
    for row in addressRef:
        if row:
            key.append(row[0])
            address.append(row[1].strip())


# Loading packages into trucks manually
truck1 = Truck("Truck 1", # Package 14 must be delivered with 15,19 and Package 20 must be delivered with 13,15
                  [1,2,13,14,15,19,20,21,27,29,30,33,34,35,37],
                  datetime(2024, 8, 23,8,0))

truck2 = Truck("Truck 2", # Packages 36,38,18,3 can only be on truck 2
                  [4,6,11,12,17,18,17,18,23,24,31,32,36,40,3,38],
                  datetime(2024,8,23,9,50)) # Packages 6 and 32 are delayed and not arriving until 9:05am 

truck3 = Truck("Truck 3",# Package 16 must be delivered with 13,19
                    [5,7,8,9,10,16,26,28,39,25,22],
                    datetime(2024,8,23,9,50)) # Packages 25 and 28 are delayed and not arriving until 9:05am 
                    # placeholder - truck 3 needs to wait until truck 1 returns

with open(distanceFile, 'r', encoding='utf-8-sig') as csvfile:
    distanceRef = csv.reader(csvfile)
    distanceRef = list(distanceRef)

def findDistance(row, column):
    if column > row:
        temp = row
        row = column
        column = temp
    distance = distanceRef[row][column]
#    print("This is the distance: ", distance)
    return float(distance)

# Gets address from packageID
def getAdresss(package_id):
    for i in range(len(packageHash.table)):
        bucket_list = packageHash.table[i]
        for key_value in bucket_list:
            key, package = key_value
            if key == package_id:
                return package.address
    return None

# Get key to know what address to reference in distance table
def getKey(package):
    package_address = getAdresss(package)
    location_key = None
    for index in address:
        if index == package_address:
            location_key = address.index(index) + 1
    if package == 0:
        location_key = 1
    return location_key

# Gets the next location to travel to
def nearestLocation(start, package_list):
    smallest_distance = float('inf')
    next_location = None
    start_key = getKey(start)
    #print(start_key)
    for package in package_list:
        id_to_key = getKey(package)
        #print(id_to_key)
        if id_to_key is not None:
            #print('Comparing: ',start_key, package)
            distance = findDistance(start_key, id_to_key)
            #print('Results: Current Challenger: ',package, distance, "Current leader: ", next_location, smallest_distance)
            if distance < smallest_distance:
                smallest_distance = distance
                next_location = package
                #print("This is the next candidate location: ", next_location)
    #print("This is the next location", next_location)
    return next_location


# ordering the route that the trucks will go in based on closest distance to current location
def deliveryRoute(truck):
    route = []
    start_point = 0
    packages_left = truck.packages[:]
    while packages_left:
        next_location = nearestLocation(start_point,packages_left)
        route.append(next_location)
        packages_left.remove(next_location)
        start_point = next_location
    return route

#print(deliveryRoute(truck1))
#print(truck1.packages[:])

#B
#print(packageHash.search(1))

# runs the trucks through delivery while keeping track of mileage, time, and status
def truck_run(truck):
    truck_list = deliveryRoute(truck)
    mileage = 0
    start = 1
    start_location = "HUB"
    start_time = truck.departTime
    current_time = datetime.now().time()
    for package in truck_list:
        package_info = packageHash.search(package)

        if package_info.package_id == '9':
            if current_time > datetime(2024,8,23,10,20):  # Time after 10:20 AM
                package_info.address = "410 S State St"
                package_info.zipcode = "84111"

        package_info.status = f"In route"

        address = getAdresss(package)
        package_key = getKey(package)

        distance = findDistance(start,package_key)
        timepast = distance/(truck.speed)
        minutes = timepast * 60
        time_delta = timedelta(minutes=minutes)
        current_time = start_time + time_delta

        package_info.departureTime = start_time.strftime("%I:%M %p")
        package_info.timeOfDelivery = current_time.strftime("%I:%M %p")
        package_info.status = f"Delivered"


        
        print(f"{truck.id} delivered package {package} to {address} from {start_location} at {current_time.strftime('%I:%M %p')} with distance {distance}")
        start_location = address
        start_time = current_time
        mileage += distance
        start = package_key


    return_distance = findDistance(start,1) # Return to hub
    mileage += return_distance
    extra_time = return_distance / truck.speed
    extra_time_minutes = extra_time * 60
    time_delta = timedelta(minutes=extra_time_minutes)
    current_time += time_delta
    if truck == truck1:
        print(f"Truck One returned to headquarters at {current_time.strftime('%I:%M %p')}")
        mileage = round(mileage,2)
        print(f"Truck One traveled {mileage} miles.")
        return mileage
    elif (truck == truck2):
        print(f"Truck Two returned to headquarters at {current_time.strftime('%I:%M %p')}")
        mileage = round(mileage,2)
        print(f"Truck Two traveled {mileage} miles.")
        return mileage
    elif (truck == truck3):
        print(f"Truck Three returned to headquarters at {current_time.strftime('%I:%M %p')}")
        mileage = round(mileage,2)
        print(f"Truck Three traveled {mileage} miles.")
        print("\nAll trucks have made their deliveries for the day and have returned to headquarters.")
        return mileage
    else:
        print(f"Unknown Truck returned to headquarters at {current_time.strftime('%I:%M %p')}")
        mileage = round(mileage,2)
        print(f"Truck Three traveled {mileage} miles.")
        print("\nAll trucks have made their deliveries for the day and have returned to headquarters.")

        return mileage

#mileage1 = truck_run(truck1)
#mileage2 = truck_run(truck2)
#mileage3 = truck_run(truck3)
#total_mileage = mileage1 + mileage2 + mileage3
#print(mileage3)

# find the truck the package is on
truck_options = [truck1, truck2, truck3]

def findTruck(packageID,trucks):
    for truck in trucks:
        if packageID in truck.packages:
            return truck.id
 
#print(findTruck(14 ,truck_options))

def print_status(input_time):
    for i in range(len(packageHash.table)):
        bucket_list = packageHash.table[i]
        for keyValue in bucket_list:
            key, package = keyValue
            if key != '0':
                time_datetime = datetime.strptime(input_time, "%I:%M %p").time()
                formatted_time = time_datetime.strftime("%H:%M")

                # package 9 is not updated until 10:20am
            if key == '9':

                if (time_datetime > datetime.strptime('10:20 am',"%I:%M %p").time()):  # Time after 10:20 AM
                        package.address = "410 S State St"
                        package.zipcode = "84111"
                elif (time_datetime < datetime.strptime('10:20 am',"%I:%M %p").time()):
                        package.address = "300 State St"
                        package.zipcode = "84103"

            truck_number = findTruck(key,truck_options)
            if package.departureTime == None:
                package.status = 'At Hub'
                
                print(f"Package:{key} on {truck_number}     Address: {package.address}            Deadline: {package.deadline}      Package Status:{package.status}")
            elif formatted_time <= package.departureTime:
                package.status = 'At hub'
                print(f"Package:{key} on {truck_number}     Address: {package.address}            Deadline: {package.deadline}      Package Status:{package.status}")
            elif formatted_time <= package.timeOfDelivery:
                package.status = 'en route'
                truck_number = findTruck(int(package_id),truck_options)
                print(f"Package:{key} on {truck_number}      Address: {package.address}            Deadline: {package.deadline}      Package Status:{package.status}")
            else:
                package.status = 'delivered'
                print(f"Package:{key} on {truck_number}      Address: {package.address}            Deadline: {package.deadline}      Package Status:{package.status} at {package.timeOfDelivery}")

print_status("10:20 pm")

# prints the status for one of the packages at any given time
def print_status_package(time,package):
    time_datetime = datetime.strptime(time, "%I:%M %p").time()
    formatted_time = time_datetime.strftime("%H:%M")
    package_info = packageHash.search(package)
    truck_number = findTruck(package,truck_options)

    # package 9 is not updated until 10:20am
    if package == '9':

        if (time_datetime > datetime.strptime('10:20 am',"%I:%M %p").time()):  # Time after 10:20 AM
            package_info.address = "410 S State St"
            package_info.zipcode = "84111"
        elif (time_datetime < datetime.strptime('10:20 am',"%I:%M %p").time()):
            package_info.address = "300 State St"
            package_info.zipcode = "84103"

    if package_info.departureTime == None:
        package_info.packageStatus = 'at hub'
        print(f"Package:{package} on {truck_number}      Address: {package_info.address}       Deadline: {package_info.deadline}     Package Status:{package_info.packageStatus}")
    elif formatted_time <= package_info.departureTime:
        package_info.packageStatus = 'at hub'
        print(f"Package:{package} on {truck_number}      Address: {package_info.address}       Deadline: {package_info.deadline}     Package Status:{package_info.packageStatus}")
    elif formatted_time <= package_info.timeOfDelivery:
        package_info.packageStatus = 'en route'
        print(f"Package:{package} on {truck_number}      Address: {package_info.address}       Deadline: {package_info.deadline}     Package Status:{package_info.packageStatus}")
    else:
        package_info.packageStatus = 'delivered'
        print(f"Package:{package} on {truck_number}      Address: {package_info.address}       Deadline: {package_info.deadline}     Package Status:{package_info.packageStatus} at {package_info.timeOfDelivery}")

#print_status_package("10:20 pm", 10)
#print_status_package("10:20 pm", 20)
#print_status_package("10:20 pm", 40)

# gives user options to look up packages and delivery status
def multiple_choice():
    options = {
        "A":"Check Status of ALL Packages at a Certain Time",
        "B":"Check Status of ONE Package at a Certain Time.",
        "C":"Exit Program"
    }

    print("Please select how you would like to proceed:")
    for letter, value in options.items():
        print(f"{letter}: {value}")

    user_input = input("Enter the letter of your choice: ").strip().upper()
    return user_input

# plays out what the user picked during multiple choice
def handle_choice(choice):

    if choice == 'A':
        a_input = input("What time would you like to view? (Please input HH:MM am/pm)")
        print_status(a_input)
        user_choice = multiple_choice()
        handle_choice(user_choice)


    elif choice == 'B':
        package_input = input("What package would you like to view?")
        time_input =  input("What time would you like to view this package? (Please input HH:MM am/pm)")
        print_status_package(time_input,package_input)
        user_choice = multiple_choice()
        handle_choice(user_choice)

    elif choice == 'C':
        print("You have choose to exit the program.")

# runs the delivery program
def deliveryPrompt():
    print("Welcome to the WGUPS Routing Program!")
    print("Running routing program.....\n")
    mileage1 = truck_run(truck1)
    mileage2 = truck_run(truck2)
    mileage3 = truck_run(truck3)
    total_mileage = mileage1 + mileage2 + mileage3
    total_mileage = round(total_mileage,2)
    print(f"\nIn total the trucks traveled {total_mileage} miles today.\n")

    user_choice = multiple_choice()
    handle_choice(user_choice)

deliveryPrompt()