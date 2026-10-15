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
print(f'Total={total:.1f}')
print(f'Average = {(total/(max_loop)):.1f}')