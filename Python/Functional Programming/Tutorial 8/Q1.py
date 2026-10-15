import functools

#B40 Income 3401 
# M40 income 7971 
# T40 income 19752

SunwayUniversityemployees = [
    { 'id' : '1020332', 'name': 'Mr. Ang', 'Salary': 8000, 'BusinessUnit': 'HR' }, 
    { 'id' : '1020396', 'name': 'Mrs. Joyce', 'Salary': 4100, 'BusinessUnit': 'Cash' }, 
    { 'id': '1013456', 'name': 'Mrs. Kavita', 'Salary': 5600, 'BusinessUnit': 'HR' }, 
    { 'id': '1085020', 'name': 'Ms. Hui Yan', 'Salary': 13000, 'BusinessUnit': 'HR' }, 
    { 'id': '1020345', 'name': 'Mr. Pathy', 'Salary': 8700, 'BusinessUnit': 'Procurement' }, 
    { 'id': '082110', 'name': 'Aaliya', 'Salary': 6800, 'BusinessUnit': 'Facilities' }
    ]

HRD_employees = [employee for employee in SunwayUniversityemployees if employee['BusinessUnit'] == 'HR']
print(HRD_employees)


def avg(salaries):
    """Calculate average - simple and clear"""
    return sum(salaries) / len(salaries)

# Extract all salaries
all_salaries = [emp['Salary'] for emp in SunwayUniversityemployees]

# Calculate average
average_salary = avg(all_salaries)
print(f"Average salary: RM {average_salary:.2f}")


def belowAverage(SunwayUniversityemployees):
    return SunwayUniversityemployees['Salary'] < average_salary

belowAverageEmployees = list(filter(belowAverage, SunwayUniversityemployees))

print(belowAverageEmployees)



