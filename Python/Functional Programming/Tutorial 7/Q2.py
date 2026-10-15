students = [{ 'id' : '17070001', 'name': 'Muhammad', 'CGPA': 3.8, 'Program': 'bse' }, 
            { 'id' : '17070002', 'name': 'Lee', 'CGPA': 3.5, 'Program': 'bcs' }, 
            { 'id': '17070003', 'name': 'Luther', 'CGPA': 3.2, 'Program': 'bcs' }, 
            { 'id': '17070004', 'name': 'Natalie', 'CGPA': 3.1, 'Program': 'bse' }, 
            { 'id': '17070005', 'name': 'AbulAllah', 'CGPA': 3.3, 'Program': 'bcns' }, 
            { 'id': '17070006', 'name': 'Munesh', 'CGPA': 3.4, 'Program': 'bse' }]

# Write a functional code in python to retrieve and print separately the CGPA of the following students: 
# the students of bse (Bachelor of Software Engineering), 
# the students of bcs (Bachelor of Computer Science) and 
# the students of bcns (Bachelor of Network and Computer Security).

def getCGPA(student):
    return student['CGPA']

BSE_studentCGPA = list(map(getCGPA, students))
BCS_studentCGPA = list(map(getCGPA, students))
BCNS_studentCGPA = list(map(getCGPA, students))

print (BSE_studentCGPA)
print (BCS_studentCGPA)
print (BCNS_studentCGPA)

# mapping is for modifying data in a function