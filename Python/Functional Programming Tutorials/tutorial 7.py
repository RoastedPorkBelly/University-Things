students = [{
    'id' : '17070001',
    'name': 'Muhammad',
    'CGPA': 3.8,
    'Program': 'bse'
    }, {
    'id' : '17070002',
    'name': 'Lee',
    'CGPA': 3.5,
    'Program': 'bcs'
    }, {
    'id': '17070003',
    'name': 'Luther',
    'CGPA': 3.2,
    'Program': 'bcs'
    }, {
    'id': '17070004',
    'name': 'Natalie',
    'CGPA': 3.1,
    'Program': 'bse'
    }, {
    'id': '17070005',
    'name': 'AbulAllah',
    'CGPA': 3.3,
    'Program': 'bcns'
    }, {
    'id': '17070006',
    'name': 'Munesh',
    'CGPA': 3.4,
    'Program': 'bse'
    }]

def is_BSEStudent(students):
    return students['Program'] == 'bse'

def is_BCSStudent(students):
    return students['Program'] == 'bcs'

def is_BCNSStudent(students):
    return students['Program'] == 'bcns'

BSEStudents = list(filter(is_BSEStudent, students))
BCSStudents = list(filter(is_BCSStudent, students))
BCNSStudents = list(filter(is_BCNSStudent, students))

def get_cgpa(students):
    return students['CGPA']

BSEstudent_cgpa = list(map(get_cgpa,BSEStudents))
BCSstudent_cgpa = list(map(get_cgpa,BCSStudents))
BCNSstudent_cgpa = list(map(get_cgpa,BCNSStudents))

SpecificStudent = [x for x in BSEStudents
if x['name']=='Muhammad']

def get_name(student):
    return student['name']

def append_with_space (str1 , str2):
    return f'{str1} {str2}'

DisplayMode ="mode2"

def process_details (func,id,name,cgpa,program):
    return func(id,name,cgpa,program)

def display_mode1(str1 , str2, str3,str4):
    return f'{str1}, {str2}, {str3}, {str4}'

def display_mode2(str1 , str2, str3,str4):
    return f'{str4} {str1} {str2} {str3}'

display = display_mode1 if DisplayMode == "mode1" else display_mode2


