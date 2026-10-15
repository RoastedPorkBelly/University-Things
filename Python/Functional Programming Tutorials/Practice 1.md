1. What arguments can you make in favor of having a single programming language for all application domains? 
	- learning curve very straightforward for everyone
	- easier collaboration between teams
	- only one compiler would be needed

2. What arguments can you make against having one universal programming language for all domains? 
	- no such thing as a one size fits all for programming

3. Besides readability, writability, reliability, and cost, name and explain another reasonable criterion that can be used to evaluate programming languages. 
	- wording: how much code is needed to express an idea
	- conciseness is preferable over wordiness: simple ideas shouldnt be expressed in many lines of code 

4. Java uses a right brace (}) to mark the end of all compound statements. What are the advantages and disadvantages of this design choice in terms of readability and writability?
	- Advantages: easy to remember and type in
	- Disadvantages: nested code harder to read without proper formatting

5. Many languages distinguish between uppercase and lowercase letters in user-defined names. What are the pros and cons of this design decision for programmers and code maintenance?
	- Pros: without distinguishing, it would be harder to differentiate classes, variables and functions
	- Cons: harder debugging and when names are too similar it is hard to differentiate as well

6. Even though modern hardware is relatively inexpensive and powerful, what are the reasons for still writing efficient programs? 
	- small inefficiencies will compound in big systems and become big errors

7. Many contemporary languages support two types of comments: • One that uses paired delimiters for multi-line comments (e.g., /* … */) • One that uses a single delimiter for one-line comments (e.g., //) Discuss the advantages and disadvantages of each in terms of reliability, readability, and writability.
	

|                                               | Advantages                 | Disadvantages                     |
| --------------------------------------------- | -------------------------- | --------------------------------- |
| single delimiter for **one-line** comments    | easy to write              | have to write // on every comment |
| paired delimiters for **multi**-line comments | easy to comment long lines | can comment out code              |
