eggs = "global"

def spam():
    print(eggs)
    eggs = "spam local"

spam()

#local variable called before assignment