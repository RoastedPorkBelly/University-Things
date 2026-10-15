usage = float(input('Monthly Data Usage: '))
if usage <=10:
    total = 15
#if usage is 10GB or less, then each GB will cost 15 RM each

else: total = (10*15) + ((usage-10)*30)

print(f'For a data usage of {usage:.2f} GB, the total amount is RM{total:.2f}')