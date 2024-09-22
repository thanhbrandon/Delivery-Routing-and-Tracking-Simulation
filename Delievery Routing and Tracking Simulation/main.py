from truck import Truck
from hashtable import HashTable
from file import File
from package import Package
from distance import Distance
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

truck_1 = Truck()

print(truck_1.numPackages)

truck_1.getNumPackages()

bestMovies = [
    [1, "CITIZEN KANE - 1941"],
    [2, "CASABLANCA - 1942"],
    [3, "THE GODFATHER - 1972"],
    [4, "GONE WITH THE WIND - 1939"],
    [5, "LAWRENCE OF ARABIA - 1962"],
    [6, "THE WIZARD OF OZ - 1939"],
    [7, "THE GRADUATE - 1967"],
    [8, "ON THE WATERFRONT- 1954"],
    [9, "SCHINDLER'S LIST -1993"],
    [10, "SINGIN' IN THE RAIN - 1952"],
    [11, "STAR WARS - 1977"]
]

myHash = HashTable()

print("\nInsert:")
myHash.insert(bestMovies[0][0], bestMovies[0][1])  # 2nd bucket; Key=1, item="CITIZEN KANE - 1941"
print(myHash.table)

myHash.insert(bestMovies[10][0], bestMovies[10][1])  # 2nd bucket as well; Key=11, item="STAR WARS - 1977"
print(myHash.table)

print("\nSearch:")
print(myHash.search(1))  # Key=1, item="CITIZEN KANE - 1941"
print(myHash.search(11))  # Key=11, item="STAR WARS - 1977"; so same bucket and Chainin is working

print("\nUpdate:")
myHash.insert(1, "Star Trek - 1979")  # 2nd bucket; Key=1, item="Star Trek - 1979"
print(myHash.table)

print("\nRemove:")
myHash.remove(1)  # Key=1, item="Star Trek - 1979" to remove
print(myHash.table)

myHash.remove(11)  # Key=11, item="STAR WARS - 1977" to remove
print(myHash.table)

# RUNTIME -> O(n^2)
def load_package_data():
    package_data = File('WGUPS Package File.csv')
    size = package_data.get_row_count()
    package_hash_table = HashTable(size)
    package_hash_table = package_data.parse_package_data()
    return package_hash_table

# RUNTIME -> O(n^2)
def load_distance_table():
    distance_table = File('WGUPS Distance Table.csv')
    raw_data = distance_table.parse_distance_data()
    d = Distance(raw_data)
    distance_data = d.clean_and_sort_data()
    return distance_data

load_package_data()
load_distance_table()