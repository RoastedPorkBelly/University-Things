g1. When might you want the compiler to ignore type differences in an expression? 
when a type is a subrange of another type, for example type1 is defined as (1-100), it should still be able to interact with other integers

2. Describe a situation in which the add operator in a programming language would not be associative.
integer overflow 
for example when the computer's max int value is 32767,
the expression 20000 + 25000 - 20000 must be calculated like this:
20000 + (25000-20000)

this is to avoid (20000 + 25000 = 45000), which will overflow the int value

3. 