# Student ID 011652606
from truck import Truck
from package import Package
from hashtable import HashTable
from datetime import datetime, timedelta

import csv

# csv file names
packageFile = "WGUPS Package File.csv"
distanceFile = "WGUPS Distance Table.csv"
addressFile = "addresses.csv"

# Initializing chaining hash table
packageHash = HashTable()

# Reading package data into hash table
with open(packageFile, 'r', encoding='utf-8-sig') as csvfile:
    # extracting each data row one by one
    csvreader = csv.reader(csvfile)
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

# Creating Distance list to reference for distances between addresses
with open(distanceFile, 'r', encoding='utf-8-sig') as csvfile:
    distanceRef = csv.reader(csvfile)
    distanceRef = list(distanceRef)

# find_distance function to find distance between two addresses
def find_distance(row, column):
    if column > row:
        temp = row
        row = column
        column = temp
    distance = distanceRef[row][column]
#    print("This is the distance: ", distance)
    return float(distance)

# Gets address from packageID
def get_address(package_id):
    for i in range(len(packageHash.table)):
        bucket_list = packageHash.table[i]
        for key_value in bucket_list:
            key, package = key_value
            if key == package_id:
                return package.address
    return None

# Get index to know what address to reference in distance table
def get_key(package):
    package_address = get_address(package)
    location_index = None
    for index in address:
        if index == package_address:
            location_index = address.index(index) + 1
    if package == 0:
        location_index = 1
    return location_index

# Gets the next location to travel to
def nearest_location(start, package_list):
    smallest_distance = float('inf')
    next_location = None
    start_index = get_key(start)
    for package in package_list:
        id_to_key = get_key(package)
        if id_to_key is not None:
            distance = find_distance(start_index, id_to_key)
            if distance < smallest_distance:
                smallest_distance = distance
                next_location = package
                #print("This is the next candidate location: ", next_location)
    #print("This is the next location", next_location)
    return next_location


# ordering the route that the trucks will go in based on closest distance to current location
def get_route(truck):
    route = []
    start_point = 0
    packages_left = truck.packages[:]
    while packages_left:
        next_location = nearest_location(start_point, packages_left)
        route.append(next_location)
        packages_left.remove(next_location)
        start_point = next_location
    return route

# runs the trucks through delivery while keeping track of mileage, time, and status
def run_deliveries(truck):
    truck_route = get_route(truck)
    mileage = 0
    start = 1
    start_location = "HUB"
    start_time = truck.departTime
    current_time = datetime.now().time()
    for package in truck_route:
        package_info = packageHash.search(package)

        if package_info.package_id == '9':
            if current_time > datetime(2024,8,23,10,20):  # Time after 10:20 AM
                package_info.address = "410 S State St"
                package_info.zipcode = "84111"

        package_info.status = f"on route"

        address = get_address(package)
        package_key = get_key(package)

        miles = find_distance(start, package_key)
        hours = miles/(truck.speed)
        minutes = hours * 60
        time_delta = timedelta(minutes=minutes)
        current_time = start_time + time_delta

        package_info.departureTime = start_time.strftime("%I:%M %p")
        package_info.timeOfDelivery = current_time.strftime("%I:%M %p")
        package_info.status = f"Delivered"

        print(f"{truck.id} delivered package {package} to {address} from {start_location} at {current_time.strftime('%I:%M %p')} with distance {miles} miles")
        start_location = address
        start_time = current_time
        mileage += miles
        start = package_key

    return_distance = find_distance(start, 1) # Return to hub
    mileage += return_distance
    extra_time = return_distance / truck.speed
    extra_time_minutes = extra_time * 60
    time_delta = timedelta(minutes=extra_time_minutes)
    current_time += time_delta
    if truck == truck1:
        print(f"Truck 1 returned to the hub at {current_time.strftime('%I:%M %p')}")
        mileage = round(mileage,2)
        print(f"Truck 1 traveled {mileage} miles.")
        return mileage
    elif truck == truck2:
        print(f"Truck 2 returned to the hub at {current_time.strftime('%I:%M %p')}")
        mileage = round(mileage,2)
        print(f"Truck 2 traveled {mileage} miles.")
        return mileage
    elif truck == truck3:
        print(f"Truck 3 returned to the hub at {current_time.strftime('%I:%M %p')}")
        mileage = round(mileage,2)
        print(f"Truck 3 traveled {mileage} miles.")
        return mileage
    else:
        print(f"Unknown Truck returned to the hub at {current_time.strftime('%I:%M %p')}")
        mileage = round(mileage,2)
        print(f"Unknown Truck traveled {mileage} miles.")
        return mileage

#mileage1 = truck_run(truck1)
#mileage2 = truck_run(truck2)
#mileage3 = truck_run(truck3)
#total_mileage = mileage1 + mileage2 + mileage3
#print(mileage3)


truck_list = [truck1, truck2, truck3]
# find_truck function finds the truck the package is on
def find_truck(packageID, trucks):
    for truck in trucks:
        if packageID in truck.packages:
            return truck.id

    return "no truck"

# print a specific package's information and status at a specified time
def get_specific_package_status(time, package):
    try:
        time_datetime = datetime.strptime(time, "%I:%M %p").time()
        formatted_time = time_datetime.strftime("%H:%M")
    except:
        print("There was an issue with the input try again.")
        handle_option('B')
    try:
        package_info = packageHash.search(int(package))
        print(package_info)
    except:
        print("Package does not exist or ID is incorrect!")
        handle_option('B')
    truck_number = find_truck(package, truck_list)

    # package 9 is not updated until 10:20am
    if package == '9':

        if time_datetime > datetime.strptime('10:20 am', "%I:%M %p").time():  # Time after 10:20 AM
            package_info.address = "410 S State St"
            package_info.zipcode = "84111"
        elif time_datetime < datetime.strptime('10:20 am', "%I:%M %p").time():
            package_info.address = "300 State St"
            package_info.zipcode = "84103"

    try:
        if package_info.departureTime is None:
            package_info.packageStatus = 'at hub'
            print(f"Package:{package:<3} on {truck_number}      Address: {package_info.address:<25}       Deadline: {package_info.deadline:<10}     Package Status:{package_info.packageStatus}")
        elif formatted_time <= package_info.departureTime:
            package_info.packageStatus = 'at hub'
            print(f"Package:{package:<3} on {truck_number}      Address: {package_info.address:<25}       Deadline: {package_info.deadline:<10}     Package Status:{package_info.packageStatus}")
        elif formatted_time <= package_info.timeOfDelivery:
            package_info.packageStatus = 'on route'
            print(f"Package:{package:<3} on {truck_number}      Address: {package_info.address:<25}       Deadline: {package_info.deadline:<10}     Package Status:{package_info.packageStatus}")
        else:
            package_info.packageStatus = 'delivered'
            print(f"Package:{package:<3} on {truck_number}      Address: {package_info.address:<25}       Deadline: {package_info.deadline:<10}     Package Status:{package_info.packageStatus} at {package_info.timeOfDelivery}")
    except:
        print("Package does not exist or ID is incorrect!")
#print_status_package("10:20 pm", 10)
#print_status_package("10:20 pm", 20)
#print_status_package("10:20 pm", 40)

# Prints all package's statuses at a specific time
def get_all_package_status(input_time):
    for i in range(len(packageHash.table)):
        bucket_list = packageHash.table[i]
        for keyValue in bucket_list:
            key, package = keyValue
            if key != '0':
                try:
                    time_datetime = datetime.strptime(input_time, "%I:%M %p").time()
                    formatted_time = time_datetime.strftime("%H:%M")
                except:
                    print("There was an issue with the input try again.")
                    handle_option('C')
                # package 9 is not updated until 10:20am
            if key == '9':

                if time_datetime > datetime.strptime('10:20 am', "%I:%M %p").time():  # Time after 10:20 AM
                        package.address = "410 S State St"
                        package.zipcode = "84111"
                elif time_datetime < datetime.strptime('10:20 am', "%I:%M %p").time():
                        package.address = "300 State St"
                        package.zipcode = "84103"

            truck_number = find_truck(key, truck_list)
            if package.departureTime is None:
                package.status = 'at Hub'

                print(f"Package:{key:<3}on {truck_number:<8}     Address: {package.address:<40}     Deadline: {package.deadline:<8} Package Status:{package.status}")
            elif formatted_time <= package.departureTime:
                package.status = 'at hub'
                print(f"Package:{key:<3}on {truck_number:<8}     Address: {package.address:<40}     Deadline: {package.deadline:<8} Package Status:{package.status}")
            elif formatted_time <= package.timeOfDelivery:
                package.status = 'on route'
                truck_number = find_truck(int(package_id), truck_list)
                print(f"Package:{key:<3}on {truck_number:<8}     Address: {package.address:<40}     Deadline: {package.deadline:<8} Package Status:{package.status}")
            else:
                package.status = 'delivered'
                print(f"Package:{key:<3}on {truck_number:<8}     Address: {package.address:<40}     Deadline: {package.deadline:<8}    Package Status:{package.status} at {package.timeOfDelivery}")

#print_status("10:20 pm")

# gives user options to run the deliveries and look up packages and delivery status
def print_options():
    options = {
        "A":"Run deliveries",
        "B":"Check status of ONE Package at a specific time.",
        "C": "Check status of ALL Packages at a specific time",
        "D":"Exit program"
    }

    print("MAIN MENU")
    for letter, value in options.items():
        print(f"{letter}: {value}")

    user_input = input("Selection (A, B, C, or D): ").strip().upper()
    return user_input

# handle_option function handles the user input from the print_options function
def handle_option(option):
    if option == 'A':
        print("Running deliveries.....\n")
        mileage1 = run_deliveries(truck1)
        mileage2 = run_deliveries(truck2)
        mileage3 = run_deliveries(truck3)
        total_mileage = mileage1 + mileage2 + mileage3
        total_mileage = round(total_mileage, 2)
        print(f"\nThe trucks completed the deliveries and traveled a total of {total_mileage} miles.\n")
        option_menu()

    elif option == 'B':
        package_input = input("Enter PackageID: ")
        time_input =  input("Enter time as HH:MM am/pm: ")
        get_specific_package_status(time_input, package_input)
        option_menu()

    elif option == 'C':
        b_input = input("Enter time as HH:MM am/pm: ")
        get_all_package_status(b_input)
        option_menu()

    elif option == 'D':
        print("Exiting Program")

    else:
        print("NOT A VALID CHOICE! TRY AGAIN!")
        option_menu()

# Prints the options and handles the user input
def option_menu():
    input = print_options()
    handle_option(input)

print("WGUPS ROUTING PROGRAM INITIALIZED")
option_menu() # Runs the option menu