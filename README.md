A.  Identify a named self-adjusting algorithm (e.g., nearest neighbor algorithm, greedy algorithm) that could be used to create your program to deliver the packages.

	The nearest neighbor algorithm could create my program and deliver the packages. This algorithm always chooses the next closest delivery address from the current address.

B.  Identify a self-adjusting data structure, such as a hash table, that could be used with the algorithm identified in part A to store the package data.
	1.  Explain how your data structure accounts for the relationship between the data components you are storing.
	
	The hash table can be used as the data structure to store the package data for the algorithm. 
	The key will be the unique package tracking number and the key will provide the bucket index. This key will be paired with a value that will store the package information

C.  Write an overview of your program in which you do the following:
	1.  Explain the algorithm’s logic using pseudocode.
	Note: You may refer to the attached “Sample Core Algorithm Overview” to complete part C1.
 
	1. Load the packages into trucks
    	2. The truck will travel to the nearest node for a delivery
    	3. The truck will travel to the next nearest node for a delivery
    	4. The truck will continue to travel to continue to do this until all packages are delivered.
  	5. The truck will come back to the hub. 	

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
   	The package weight and delivery status would be bad keys because looking them up in a hash table would be difficult. 


