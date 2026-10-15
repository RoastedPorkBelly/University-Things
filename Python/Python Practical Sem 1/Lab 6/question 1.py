list = []
counter = 1
while counter <=5:
    num = float(input('Enter a number: '))
    list.append(num)
    counter +=1

list.sort()
print('my_list = ',list)