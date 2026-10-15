1. What is a data type? What are some of the design issues that you should consider when you define a data type?? 
	collection of data objects and operations
	design issue: what operations are defined and specified

2. What is a primitive data-type? Give three examples of primitive data-type in Java. 
	data types that arent defined in other data types
	e.g. byte, int, short, long

3. What is a string data type? Is the string data type primitive in C language? Justify your answer and give an example. 
	sequences of characters
	no because characters are used to store data
	e.g. char str[] = "PRG2205";

4. Provide a suitable data type for a student ID in Elearn system in Sunway University. Justify your answer. 
	string, because it can read 0's in front of numbers

5. A student program may be of the following values: BCS, BSE, BCNS and BIT. 
	• Provide a suitable data type for a student program in Sunway University. Justify your answer. 
		enum, because the values will be constant and easily changed in the code, and it will be easier to detect errors
	• Give an example of an implementation in one language. 
		no
	• Discuss some design issues for the selected data type. 
		


6. What is an array data type? What is a slice of an array? Given the following Python declarations, where PRG2205marks represents the marks for PRG2205 students and PRG2205marksdetailed represents the detailed marks 
	PRG2205marks = [79, 80, 68, 71, 75] 
	PRG2205marksdetailed = [[15, 12, 12, 40], [15, 12, 12, 41], [12, 9, 9, 38], [12, 9, 9, 41], [12, 11, 11, 41]] 
	• Obtain the subject mark for the second student. 
		PRG2205marks[1] = 80
	• Obtain the subject marks for the third and fourth students. 
		PRG2205marks[2,4] 68, 71
	• Obtain the first two subject detailed marks for the first student. 
		15,12
	
	Array = homogenous aggregates of data elements 
	Array Slice= section of the array


7. What are the arguments for and against representing Boolean values as single bits in memory? 
	Pro = space efficient
	Con = slower access if stored in bytes

8. How does a decimal value waste memory space?
	four binary bits to store one decimal digit, but those four bits can store more information