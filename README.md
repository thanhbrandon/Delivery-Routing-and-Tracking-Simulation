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

	The nearest neighbor algorithm could create my program and deliver the packages. This algorithm works by always choosing the best option at its current state. In this scenario, the delivery truck will always select to go to the closest location based on its current position. 

B.  Identify a self-adjusting data structure, such as a hash table, that could be used with the algorithm identified in part A to store the package data.
	1.  Explain how your data structure accounts for the relationship between the data components you are storing.
	
	The hash table can be used as the data structure to store the package data for the algorithm. 
	The key will be the unique package tracking number and the key will provide the bucket index. This key will be paired with the package information.
 	The package information will be the package's delivery address and delivery status.

C.  Write an overview of your program in which you do the following:
	1.  Explain the algorithm’s logic using pseudocode.
	Note: You may refer to the attached “Sample Core Algorithm Overview” to complete part C1.
  	
	1. Load the packages into trucks
    	2. The truck will travel to the nearest node for a delivery
    	3. The truck will travel to the next nearest node for a delivery
    	4. The truck will continue to travel to continue to do this until all packages are delivered.
  	5. The truck will come back to the hub. 

 	totalDistance = 0
  	currentLocation = Packages[hub]
   	while totalPackages > 0
		nextLocation = packages[1]
    		For i in packages
      			if package[i].distance - currentLocation.distance < nextLocationDistance
	 			nextLocationDistance = package[i].distance - currentLocation.distance
	 			nextLocation = packages[I]
     			package.drop[nextLocation]
			totalDistance = totalDistance + nextlocation.distance[0]

3.  Describe the programming environment you will use to create the Python application, including both the software and hardware you will use.

	The software I will be using is the Visual Studio Code IDE, which can be run on any IDE that can code in Python.
	The hardware I will use is a personal desktop computer.

4.  Evaluate the space-time complexity of each major segment of the program and the entire program using big-O notation.

 	The space complexity will be O(n).

6.  Explain the capability of your solution to scale and adapt to a growing number of packages.

	The nearest neighbor algorithm is efficient in terms of space but can be quite costly in terms of time complexity as the number of locations increases.

7.  Discuss why the software design would be efficient and easy to maintain.

	My code should be efficient since it only considers the current state of the truck. 
    
9.  Describe both the strengths and weaknesses of the self-adjusting data structure (e.g., the hash table).

    	A weakness with hash tables is that collision can occur. A resolution to this issue is chaining. 

    	A strength of a hash table is that it has fast access times. The average case is O(1). The worst case is O(N) if there are multiple collisions. 
    
11.  Justify the choice of a key for efficient delivery management from the following components:
	•delivery address
	•delivery deadline
	•delivery city
	•delivery zip code
	•package ID
	•package weight
	•delivery status (i.e., at the hub, en route, or delivered), including the delivery time

 	The key should be unique, therefore the package ID will be used as the key. 
  	Since the hub is located in Utah, delivery address, delivery city, and delivery zip code would be bad keys. This is because the delivery address would cause multiple collisions.
   	The package weight and delivery status would also cause multiple collisions, since multiple packages can share the same status and weigh the same.
	The delivery deadline would also serve as a bad key because multiple packages can share the same deadline and cause collisions. 


