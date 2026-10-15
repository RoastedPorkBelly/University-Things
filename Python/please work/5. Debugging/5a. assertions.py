#Assert statements are meant to catch programmer errors.


#assert statement will do nothing
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
print(ages)
#[15, 17, 22, 26, 47, 54, 57, 73, 80, 92]
assert ages[0] <= ages[1] #first on list less than second on list

#assert false, error shown
# ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
# ages.reverse()
# ages
# assert ages[0] <= ages[1] 