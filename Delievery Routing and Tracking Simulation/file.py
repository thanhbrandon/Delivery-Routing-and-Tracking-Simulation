import csv
from hashtable import HashTable
from package import Package

# Total runtime: O(n) 
class File:
    
    def __init__(self, file):
        self.file = file
        self.row_count = 0

    def get_row_count(self):
        for line in self.file:
            self.row_count += 1
        return self.row_count

    def parse_package_data(self):
        hash_table = HashTable(self.get_row_count())  # initiate hash table using num rows

        with open(self.file, mode='r', encoding='utf-8-sig') as csv_data:
            csv_data.seek(0)  # since we read the file once already we want to make sure we reset the pointer
            data = csv.reader(csv_data, delimiter=',')
            for skip in range(8): # Skip header rows
                next(data)
            for row in data:
                key = row[0]
                package_id = row[0]
                address = row[1]
                city = row[2]
                state = row[3]
                zip_code = row[4]
                delivery_time = row[5]
                weight = row[6]
                status = 'At HUB'
                notes = row[7]

                p = Package(package_id, address, city, state, zip_code, delivery_time, weight, status, notes)

                hash_table.insert(key, p)  # add the key/values to the hash table

        return hash_table

    def parse_distance_data(self):
        with open(self.file, mode='r', encoding='utf-8-sig', newline='') as csv_data:
            csv_data.seek(0)  # since we read the file once already we want to make sure we reset the pointer
            data = csv.reader(csv_data, delimiter=',')

            raw_data = []
            for row in data:
                if row[0] == '5383 S 900 East #104':
                    row[0] = '5383 South 900 East #104'
                raw_data.append(row)

            return raw_data