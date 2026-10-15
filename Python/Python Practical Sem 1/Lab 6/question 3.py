forward_list = []
reverse_list=[]
counter = 1
total = 0
max_loop = 5
while counter <= max_loop:
    num = float(input('Enter a number: '))
    forward_list.append(num)
    total+=num
    counter +=1

forward_list.sort()
print('forward_list = ',forward_list)

counter =  max_loop -1
while counter >= 0:
    reverse_list.append(forward_list[counter])
    counter = counter -1

print('reverse_list = ', reverse_list)
