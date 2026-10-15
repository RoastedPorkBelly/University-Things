#   1.  A variable in the global scope (that is, outside all functions) is always a global variable.

eggs = "global" #global variable

#   2.  A variable in a function with a global statement is always a global variable in that function.
def spam():
    global eggs #uses the global variable 
    eggs = "spam"

#   3.  Otherwise, if a function uses a variable in an assignment statement, it is a local variable.
def bacon():
    eggs = "bacon"  #local variable

#   4.  However, if the function uses a variable but never in an assignment statement, it is a global variable.
def ham():
    print(eggs) #global variable

spam()
bacon()
print(eggs)