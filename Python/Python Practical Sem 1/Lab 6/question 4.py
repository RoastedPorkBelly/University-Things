list = []
counter = 1
total = 0
max_loop = 5
while counter <= max_loop:
    num = float(input('Enter a number: '))
    list.append(num)
    total+=num
    counter +=1

list.sort()
print('my_list = ',list)

counter = max_loop -1
while counter >=0:
    del list[counter]
    print('My list= ', list)
    counter= counter -1