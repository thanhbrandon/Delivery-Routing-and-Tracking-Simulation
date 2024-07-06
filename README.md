A.  Identify a named self-adjusting algorithm (e.g., nearest neighbor algorithm, greedy algorithm) that could be used to create your program to deliver the packages.

	The nearest neighbor algorithm could create my program and deliver the packages. This algorthim works by traveling to the nearest node in respect to the current node.

B.  Identify a self-adjusting data structure, such as a hash table, that could be used with the algorithm identified in part A to store the package data.
1.  Explain how your data structure accounts for the relationship between the data components you are storing.
	
	The hash table can be used as the data structure to store the package data for the algorithm. 
	The key will be the unique package tracking number and the key will provide the bucket index. 

C.  Write an overview of your program in which you do the following:
1.  Explain the algorithm’s logic using pseudocode.
	1. Load the packages
    	2. 
    	3.     
    	4.    
   
 
Note: You may refer to the attached “Sample Core Algorithm Overview” to complete part C1.


2.  Describe the programming environment you will use to create the Python application, including both the software and hardware you will use.

  	The software I will be using is the Visual Studio Code IDE, but it can be run on any IDE that can code in python.
	The harware I will use is a personal destop computer.

4.  Evaluate the space-time complexity of each major segment of the program and the entire program using big-O notation.

 	The space complexity will be O(n)

6.  Explain the capability of your solution to scale and adapt to a growing number of packages.

	My solution will scale linearly as the number of packages grows.

7.  Discuss why the software design would be efficient and easy to maintain.

	My code should be efficient since it is only taking into account the current state of the truck. 
    
9.  Describe both the strengths and weaknesses of the self-adjusting data structure (e.g., the hash table).

    	A weakness with hash tables is that collision can occur. A resolution to this issue is chaining. 

    	A strength of a hash table is that it has fast access times. The average case is O(1). Worst case is O(N) if there are mulitple collisions. 
    
11.  Justify the choice of a key for efficient delivery management from the following components:
	•delivery address
	•delivery deadline
	•delivery city
	•delivery zip code
	•package ID
	•package weight
	•delivery status (i.e., at the hub, en route, or delivered), including the delivery time

 	The key should be unique and therefore the package ID will be used as the key. 


