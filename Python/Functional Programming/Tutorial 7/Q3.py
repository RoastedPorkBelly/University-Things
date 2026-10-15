students = [{ 'id' : '17070001', 'name': 'Muhammad', 'CGPA': 3.8, 'Program': 'bse' }, 
            { 'id' : '17070002', 'name': 'Lee', 'CGPA': 3.5, 'Program': 'bcs' }, 
            { 'id': '17070003', 'name': 'Luther', 'CGPA': 3.2, 'Program': 'bcs' }, 
            { 'id': '17070004', 'name': 'Natalie', 'CGPA': 3.1, 'Program': 'bse' }, 
            { 'id': '17070005', 'name': 'AbulAllah', 'CGPA': 3.3, 'Program': 'bcns' }, 
            { 'id': '17070006', 'name': 'Munesh', 'CGPA': 3.4, 'Program': 'bse' }]

# Write a functional code in python to search for a specific bse student by name (i.e. Muhammad) 
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

print (appendWithSpace(getName(specificStudent[0]), getCGPA(specificStudent[0])))



