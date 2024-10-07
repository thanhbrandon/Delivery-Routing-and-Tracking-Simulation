Scenario

	This task is the planning phase of the WGUPS Routing Program.
	The Western Governors University Parcel Service (WGUPS) needs to determine an efficient route and delivery distribution for their daily local deliveries (DLD) because packages are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day. Each package has specific criteria and delivery requirements that are listed in the attached “WGUPS Package File.”
	Your task is to determine an algorithm, write code, and present a solution where all 40 packages will be delivered on time while meeting each package’s requirements and keeping the combined total distance traveled under 140 miles for all trucks. The specific delivery locations are shown on the attached “Salt Lake City Downtown Map,” and distances to each location are given in the attached “WGUPS Distance Table.” The intent is to use the program for this specific location and also for many other cities in each state where WGU has a presence. As such, you will need to include detailed comments to make your code easy to follow and to justify the decisions you made while writing your scripts.
	The supervisor should be able to see, at assigned points, the progress of each truck and its packages by any of the variables listed in the “WGUPS Package File,” including what has been delivered and at what time the delivery occurred.

Assumptions

	•  Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.
	•  The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.
	•  There are no collisions.
	•  Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.
	•  Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed.
	•  The delivery and loading times are instantaneous (i.e., no time passes while at a delivery or when moving packages to a truck at the hub). This time is factored into the calculation of the average speed of the trucks.
	•  There is up to one special note associated with a package.
	•  The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S. State St., Salt Lake City, UT 84111) until 10:20 a.m.
	•  The distances provided in the “WGUPS Distance Table” are equal regardless of the direction traveled.
	•  The day ends when all 40 packages have been delivered.

A.  Identify a named self-adjusting algorithm (e.g., nearest neighbor algorithm, greedy algorithm) that could be used to create your program to deliver the packages.

	The nearest neighbor algorithm could create my program and deliver the packages. This algorithm works by always choosing the best option at its current state.
	In this scenario, the delivery truck will be loaded in the order of shortest distance between packages and then delivered in the order it was loaded into the truck.

B.  Identify a self-adjusting data structure, such as a hash table, that could be used with the algorithm identified in part A to store the package data.
	1.  Explain how your data structure accounts for the relationship between the data components you are storing.
	
	The hash table can be used as the data structure to store the package data for the algorithm. 
	The key will be the unique package tracking number, and the key will provide the bucket index. This key will be paired with the package information.
 	The package information will be the package's delivery address and delivery status.

C.  Write an overview of your program in which you do the following:
	1.  Explain the algorithm’s logic using pseudocode.
	Note: You may refer to the attached “Sample Core Algorithm Overview” to complete part C1.
  	
		Import Truck
		Import Package
		
		LoadTrucks
			For packages in packages
				Load truck with package with the shortest distance to the last package
		
		DeliverPackages
			While all packages in truck are not delivered
				Deliever packages in order added to the truck
			Return to Hub

	2.  Describe the programming environment you will use to create the Python application, including both the software and hardware you will use.
		IDE:				PyCharm Community Edition 2024.2.1
		Product Version: 	242.21829.153
		Python:				v.3.12

		Hardware:			Processor	AMD Ryzen 7 5800H with Radeon Graphics 3.20 GHz
							Installed RAM	16.0 GB (15.4 GB usable)
				 			System type	64-bit operating system, x64-based processor
		
	3.  Evaluate the space-time complexity of each major segment of the program and the entire program using big-O notation.

 		The space complexity will be O(n). It is linear because the space taken grows linearly with the number of packages added. 
		The time complexity will be O(n). The hash table to insert, remove, and search for objects will have a time-complexity of O(1). However, the iteration of the objects to determine the order of delivery is O(n). 
		Therefore, the overall time complexity will be O(n). 

	4.  Explain the capability of your solution to scale and adapt to a growing number of packages.

        Hash tables are fully capable of scaling with a growing number of packages. If the hash table reaches its limit, it would be resized with double the capacity.
		
	5.  Discuss why the software design would be efficient and easy to maintain.

		The nearest neighbor algorithm is a greedy algorithm, so while it won't always find the overall best solution it will find the best solution in the moment which will make the overall solution better than randomly selecting deliveries. 
    	The software is easy to maintain because of the modularity of the design. If a specific element (truck, package, algorithm) needs to be enhanced, it can be modified in isolation of the other pieces of the code

	6.  Describe both the strengths and weaknesses of the self-adjusting data structure (e.g., the hash table).

    	A weakness with hash tables is that collision can occur. A resolution to this issue is chaining. 
		Another weakness is the resizing may result in excess capacity and the hash table may have many empty buckets that take up space. 
    	A strength of a hash table is that it has fast access times. The average case is O(1). The worst case is O(N) if there are multiple collisions. 
    
	7.  Justify the choice of a key for efficient delivery management from the following components:
       •delivery address
       •delivery deadline
       •delivery city
       •delivery zip code
       •package ID
       •package weight
       •delivery status (i.e., at the hub, en route, or delivered), including the delivery time

		The key should be unique, therefore the package ID will be used as the key. 
		Since the hub is in Utah, delivery address, delivery city, and delivery zip code would be bad keys. This is because the delivery address would cause multiple collisions.
		The package weight and delivery status would also cause multiple collisions, since multiple packages can share the same status and weigh the same.
		The delivery deadline would also serve as a bad key because multiple packages can share the same deadline and cause collisions. 

A.  Develop a hash table, without using any additional libraries or classes, that has an insertion function that takes the package ID as input and inserts each of the following data components into the hash table:
	•   delivery address
	•   delivery deadline
	•   delivery city
	•   delivery zip code
	•   package weight
	•   delivery status (i.e., at the hub, en route, or delivered), including the delivery time


B.  Develop a look-up function that takes the package ID as input and returns each of the following corresponding data components:
	•   delivery address
	•   delivery deadline
	•   delivery city
	•   delivery zip code
	•   package weight
	•   delivery status (i.e., at the hub, en route, or delivered), including the delivery time
 	ChainingHashTable has a search function that takes the package ID and returns the delivery address, delivery deadline, delivery city, delivery zip code, package weight, delivery status and any notes. 


C.  Write an original program that will deliver all packages and meet all requirements using the attached supporting documents “Salt Lake City Downtown Map,” “WGUPS Distance Table,” and “WGUPS Package File.”
	1.  Create an identifying comment within the first line of a file named “main.py” that includes your student ID.
	Refer to main.py line 1
	2.  Include comments in your code to explain both the process and the flow of the program.
	Refer to code

D.  Provide an intuitive interface for the user to view the delivery status (including the delivery time) of any package at any time and the total mileage traveled by all trucks. (The delivery status should report the package as at the hub, en route, or delivered. Delivery status must include the time.)
	1.  Provide screenshots to show the status of all packages loaded onto each truck at a time between 8:35 a.m. and 9:25 a.m.
	
	2.  Provide screenshots to show the status of all packages loaded onto each truck at a time between 9:35 a.m. and 10:25 a.m.
	
	3.  Provide screenshots to show the status of all packages loaded onto each truck at a time between 12:03 p.m. and 1:12 p.m.	
 
E.  Provide screenshots showing successful completion of the code that includes the total mileage traveled by all trucks.
	
F.  Justify the package delivery algorithm used in the solution as written in the original program by doing the following:
	1.  Describe two or more strengths of the algorithm used in the solution.
	2.  Verify that the algorithm used in the solution meets all requirements in the scenario.
	3.  Identify two other named algorithms that are different from the algorithm implemented in the solution and would meet all requirements in the scenario.
		a.  Describe how both algorithms identified in part F3 are different from the algorithm used in the solution.

G.  Describe what you would do differently, other than the two algorithms identified in part F3, if you did this project again, including details of the modifications that would be made.

H.  Verify that the data structure used in the solution meets all requirements in the scenario.
	1.  Identify two other data structures that could meet the same requirements in the scenario.
		a.  Describe how each data structure identified in H1 is different from the data structure used in the solution.
