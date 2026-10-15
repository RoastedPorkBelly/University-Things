def oddRecursive(n):
    
    if n>20:
        return
    
    if n % 2 == 1:
        print(n)
    
    oddRecursive(n+1)

print (oddRecursive(0))