yearlyIncome = int(input("Yearly Income: "))

if 0<=yearlyIncome<=2500:
    taxRate = 0

elif 2501<=yearlyIncome<=10000:
    taxRate = 0.05

elif 10001<=yearlyIncome<=50000:
    taxRate = 0.15

elif yearlyIncome>=50001:
    taxRate = 0.25

print("Your tax in RM: ", round(yearlyIncome*taxRate,2)) #this works
print(f'Your tax is RM {(yearlyIncome*taxRate):.2f}') 
#this also works, use this one so you can put in the equations without having to create an extra 'output' variable to print
