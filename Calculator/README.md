##### This project perform calculator that not only adds, subtracts, division and multiplies, but is also smart enough to remember your previous calculations.
##### A general expression can contain many parentheses and operations with different priorities.
How it works:
- If a user enters only a single number, the program should print the same number.
- It supports both unary and binary minus operators.
- The program prints Invalid expression in cases when the given expression has an invalid format. 
If a user enters an invalid command, the program prints Unknown command.
- /help command prints information about your program. When the command /exit is entered, then stop.
- Store results in variables and then operating on them.
- The variable is checked for correctness. If the user inputs an invalid variable name, then the output should be "Invalid identifier".
- If a variable is valid but not declared yet, the program should print "Unknown variable".
- If the part after the "=" is wrong program print "Invalid assignment". 

#####Examples:
> 8
8
> -2 + 4 - 5 + 6
3
> 9 +++ 10 -- 8
27
> 3 --- 5
-2
> abc
Invalid expression
> 123+
Invalid expression
> +15
15
> 18 22
Invalid expression
> /go
Unknown command
> b = a
> v=   7
> n =9
> count = 10
> a = 1
> a = 2
> a = 3
> a
3
> a2a
Invalid identifier
> n1 = a2a
Invalid identifier
> n = a2a
Invalid assignment
> a  =  3
> b= 4
> c =5
> a + b - c
2
> b - c + 4 - a
0
> a = 800
> a + b + c
809
> BIG = 9000
> BIG
9000
> big
Unknown variable
> 8 * 3 + 12 * (4 - 2)
48
> 2 - 2 + 3
3
> 4 * (2 + 3
Invalid expression
> -10
-10
> a=4
> b=5
> c=6
> a*2+b*3+c*(2+3)
53
> 1 +++ 2 * 3 -- 4
11
> 3 *** 5
Invalid expression
> 4+3)
> /exit
Bye!
