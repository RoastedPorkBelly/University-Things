# user = input("Username: ")
# pw = input("Password: ")

# if user == "Logan":
#     print ("Hello Logan")

#     if pw == "123":
#         print("correct password")
#     else: 
#         print("wrong password")
# else:
#     print("user not found")

name = input("Name: ")
age = int(input("Age: "))

if name == "Logan":
    print("Hello Logan")

#less than 10
elif age < 10: 
    print("go away kid")
    
#equal to 19
elif age == 19:
    print ("Access granted")

#more than 1000
elif age > 1000:
    print ("enter a real age")

#more than 50
elif age > 50:
    print ("maybe if u were a few decades younger")


# spam = int(input("Enter 1 or 2 for a surprise: "))

# if spam == 1:
#     print ("Hellow!")
# elif spam == 2: 
#     print ("Howdy!")
# else: 
#     print ("Greetings! no surprise for u")