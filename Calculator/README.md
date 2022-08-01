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

##### Examples:  I - input, O- Output\
I: 8\
O: 8\
I: -2 + 4 - 5 + 6\
O: 3\
I: 9 +++ 10 -- 8\
O: 27\
I: 3 --- 5\
O: -2\
I: abc\
O: Invalid expression\
I: 123+\
O: Invalid expression\
I: +15\
O: 15\
I: 18 22\
O: Invalid expression\
I: /go\
O: Unknown command\
I: b = a\
I: v=   7\
I: n =9\
I: count = 10\
I: a = 1\
I: a = 2\
I: a = 3\
I: a\
O: 3\
I: a2a\
O: Invalid identifier\
I: n1 = a2a\
O: Invalid identifier\
I: n = a2a\
O: Invalid assignment\
I: a  =  3\
I: b= 4\
I: c =5\
I: a + b - c\
O: 2\
I: b - c + 4 - a\
O: 0\
I: a = 800\
I: a + b + c\
O: 809\
I: BIG = 9000\
I: BIG\
O: 9000\
I: big\
O: Unknown variable\
I: 8 * 3 + 12 * (4 - 2)\
O: 48\
I: 2 - 2 + 3\
O: 3\
I: 4 * (2 + 3\
O: Invalid expression\
I:  -10\
O: -10\
I: a=4\
I: b=5\
I: c=6\
I: a*2+b*3+c*(2+3)\
O: 53\
I: 1 +++ 2 * 3 -- 4\
O: 11\
I: 3 *** 5\
O: Invalid expression\
I: 4+3)\
O: Invalid expression\
I: /exit\
O: Bye!\
