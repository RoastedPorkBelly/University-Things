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

#filtering is for selecting data by checking conditions

# 2. Write a functional code in python to retrieve and print separately the CGPA of the following students: 
# the students of bse (Bachelor of Software Engineering), 
# the students of bcs (Bachelor of Computer Science) and 
# the students of bcns (Bachelor of Network and Computer Security).

def getCGPA(student):
    return student['CGPA']

BSE_studentCGPA = list(map(getCGPA, students))
BCS_studentCGPA = list(map(getCGPA, students))
BCNS_studentCGPA = list(map(getCGPA, students))

print ("Question 2: \n")
print (BSE_studentCGPA)
print (BCS_studentCGPA)
print (BCNS_studentCGPA)

# mapping is for modifying data in a function

# 3. Write a functional code in python to search for a specific bse student by name (i.e. Muhammad) 
# and print his details represented as his name followed by his cgpa.

def is_BSEstudent(students):
    return students ['Program'] == 'bse'

BSE_studentList = list(filter(is_BSEstudent, students))


specificStudent = [x for x in BSE_studentList if x['name'] == 'Muhammad']


def getName (student):
    return student ['name']

def getCGPA (student):
    return student ['CGPA']

def appendWithSpace(str1, str2):
    return f'{str1} {str2}'

print("Question 3: \n")
print (appendWithSpace(getName(specificStudent[0]), getCGPA(specificStudent[0])))