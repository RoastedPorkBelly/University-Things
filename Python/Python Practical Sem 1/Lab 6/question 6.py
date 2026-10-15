list = []
counter = 1
total = 0
max_loop = 5
while counter <= max_loop:
    num = str(input('Enter your data: '))
    list.append(num)
    counter +=1

print('my_list = ',list)

counter = max_loop -1
while counter >=0:
    if counter%2==0:
        del list[counter]
        print('My list= ', list)
    counter= counter -1