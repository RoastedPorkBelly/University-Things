1. What is a reserved word? 
	a special word that cannot be used as a name

2. How ca a variable be characterized? 
	 name, address, value, type, lifetime, scope

3. What is static binding and how is different from dynamic binding? 
	static = before run time, unchanged with execution
	dynamic = during execution, can change with execution

4. What is the lifetime of a variable? 
	time where variable is bound to a specific memory location, ends when unbound

5. What are the advantages and disadvantages of **dynamic type binding** in some languages (i.e. JavaScript, Python)? 
	Pros: more flexibility
	Example: a program can handle any numeric data using dynamic binding, by binding the variable the data is stored to the correct type
	
	Cons: error detection less reliable, cost during execution high, execution takes longer due to pure interpretation

5. What is a static ancestor of a subprogram? What is a dynamic ancestor of a subprogram?
	Static Ancestor: any function that contains the subprogram
	Example: function B is written inside function A, so A is the static ancestor
	
	Dynamic Ancestor: any function that **was called and still running** before the subprogram was called
	
	`main() {`
		`A();`
	`}`
	
	`A() {`
		`B();`
	`}`
	
	`B() {`
		`// we are here`
	`}` 



7. Consider the following JavaScript skeletal program: 
![[!Images/Pasted image 20251201154151.png]]
main calls sub1
sub1 calls sub2
sub3 calls nothing

a. Assuming static scoping, in the following, which declaration of x is the correct one for a reference to x? 

static = where functions are written/nested

sub1 nearest x is inside sub1
sub2 nearest enclosing `x` is also **the `x` in `sub1`**.
sub3 only visible x is the global x

b. Repeat part a, but assume dynamic scoping.
read from call stack: main > sub1 > sub2> sub3

sub1 uses its own x
sub2 has no x, looks to sub1 for x
sub3 has no x, looks to sub2 for x, looks to sub1 for x


8. Consider the following JavaScript program: 
![[!Images/Pasted image 20251201154224.png]]
List all the variables, along with the program units where they are declared, that are visible in the bodies of sub1, sub2, and sub3, assuming static scoping is used.

sub1: a(sub1), y(sub1), z(sub1), x(global)

sub2: a, b, z, 
global: x
sub1: y

sub3: a, x, w
global: y, z
