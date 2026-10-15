import functools 

students = [{ 'id' : '17070001', 'name': 'Muhammad', 'CGPA': 3.8, 'Program': 'bse' }, 
            { 'id' : '17070002', 'name': 'Lee', 'CGPA': 3.5, 'Program': 'bcs' }, 
            { 'id': '17070003', 'name': 'Luther', 'CGPA': 3.2, 'Program': 'bcs' }, 
            { 'id': '17070004', 'name': 'Natalie', 'CGPA': 3.1, 'Program': 'bse' }, 
            { 'id': '17070005', 'name': 'AbulAllah', 'CGPA': 3.3, 'Program': 'bcns' }, 
            { 'id': '17070006', 'name': 'Munesh', 'CGPA': 3.4, 'Program': 'bse' }]

# 1. Write a functional code in python to retrieve and print separately: 
# the students of bse (Bachelor of Software Engineering), 
# the students of bcs (Bachelor of Computer Science) 
# and the students of bcns (Bachelor of Network and Computer Security).

def is_BSEstudent(students):
    return students ['Program'] == 'bse'

def is_BCSstudent(students):
    return students ['Program'] == 'bcs'

def is_BCNSstudent(students):
    return students ['Program'] == 'bcns'

BSE_studentList = list(filter(is_BSEstudent, students))
BCS_studentList = list(filter(is_BCSstudent, students))
BCNS_studentList = list(filter(is_BCNSstudent, students))

print ("Question 1: \n")
print (BSE_studentList, "\n")
print (BCS_studentList, "\n")
print (BCNS_studentList, "\n")
print()

#filtering is for selecting data against a condition

# 2. Write a functional code in python to retrieve and print separately the CGPA of the following students: 
# the students of bse (Bachelor of Software Engineering), 
# the students of bcs (Bachelor of Computer Science) and 
# the students of bcns (Bachelor of Network and Computer Security).

def getCGPA(students):
    return students['CGPA']

BSE_studentCGPA = list(map(getCGPA, BSE_studentList))
BCS_studentCGPA = list(map(getCGPA, BCS_studentList))
BCNS_studentCGPA = list(map(getCGPA, BCNS_studentList))

print ("Question 2: \n")
print (BSE_studentCGPA)
print (BCS_studentCGPA)
print (BCNS_studentCGPA)

# mapping is for modifying every piece of data in a sequence

# 3. Write a functional code in python to search for a specific bse student by name (i.e. Muhammad) 
# and print his details represented as his name followed by his cgpa.

specificStudent = [x for x in BSE_studentList if x['name'] == 'Muhammad']


def getName (student):
    return student ['name']

def appendWithSpace(str1, str2):
    return f'{str1} {str2}'

print("Question 3: \n")
print(appendWithSpace
       (getName(specificStudent[0]), getCGPA(specificStudent[0]))
    )

# 4. Write a functional code in python to print the details of a specific student depending on a specific printing mode/option. 
# (For example, one might prefer to print the student details starting with his program, 
# and someone else might prefer to print the student details starting with his name).

##list comprehension is joining map and filter

def processDetails (function, id, name, CGPA, program):
    return function(id, name, CGPA, program)

#starting with name
def display1 (str1, str2, str3, str4):
    return (str1, str2, str3, str4)

#starting with program
def display2 (str1, str2, str3, str4):
    return (str4, str1, str2, str3) 

displayMode = "mode1" #Toggle between mode1 and mode2
display = display1 if displayMode == "mode1" else display2

print("Question 4: ")
print(
    processDetails(display, 
    specificStudent[0]['id'], 
    specificStudent[0]['name'], 
    specificStudent[0]['CGPA'], 
    specificStudent[0]['Program'])
    )

# 5. Write a functional code in python to obtain the average cgpa of all students, bse students, bcs students and bcns students. 
def getSum (acc, x):
    return acc + x

studentCGPA = list(map(getCGPA, students)) #transform into list of CGPAs

#Total CGPA
#reduce adds first two numbers (acc and x), result is acc and added to third number(x)

totalCGPA = functools.reduce(getSum, studentCGPA) 
totalCGPA_BCE = functools.reduce(getSum, BSE_studentCGPA)
totalCGPA_BCS = functools.reduce(getSum, BCS_studentCGPA)
totalCGPA_BCNS = functools.reduce(getSum, BCNS_studentCGPA)

#Average CGPA
#sum/total divided by length of studentGPA
averageCGPA = totalCGPA/len(studentCGPA)
averageCGPA_BCE = totalCGPA_BCE/len(BSE_studentCGPA)
averageCGPA_BCS = totalCGPA_BCS/len(BCS_studentCGPA)
averageCGPA_BCNS = totalCGPA_BCNS/len(BCNS_studentCGPA)

print("Question 5: \n")
print("Average", averageCGPA)
print("BSE", averageCGPA_BCE)
print("BCS", averageCGPA_BCS)
print("BCNS", averageCGPA_BCNS)

# 6. Create a list of functions that has the following functions: 
# a function to convert a specific student program to upper case and 
# a function to get the detailed program (i.e. return bachelor of software engineering for bse). 
# Apply that list on the program of the specific student program (obtained in Question 3) 
# to retrieve the program in upper case form followed by detailed specific program. 
# (i.e. BSE Bachelor of Software Engineering) 
# Tip: Use the following code to get every returned value from every applied/called function individually. 

print("Question 6: ")

def getFullProgramName (pName):
    if pName == 'bse' :
        return 'Bachelor of Software Engineering'
    if pName == 'bcs':
        return 'Bachelor of Computer Science'
    if pName == 'bcns':
        return 'Bachelor of Cyber Security'

function_list = [str.upper, getFullProgramName]

studentProgram = specificStudent[0]['Program']
print (studentProgram)

def funcs_apply(obj, func_list):
    return [func(obj)for func in func_list]

detailed = funcs_apply(studentProgram, function_list)
niceAndDetailed = appendWithSpace(detailed[0], detailed[1])

print(niceAndDetailed)


# 3. Print the student names of bse program one by one. Use recursion for that.
def print1by1(list, x):
    if x < 0:
        return
    print(list[x]['name'])
    print1by1(list, x-1)

print("Question 7: \n")
print1by1(BSE_studentList, len(BSE_studentList)-1)
