class Calculator:

    def __init__(self, variables):
        self.variables = variables

    def determine_operator(self, operator):
        minus = operator.count("-")
        if minus % 2 == 0:
            return "+"
        else:
            return "-"

    def construct_math_operation(self, signs):
        for i in range(len(signs)):
            try:
                if signs[i].isalpha():
                    signs[i] = int(self.variables[signs[i]])
                else:
                    signs[i] = int(signs[i])
            except ValueError:
                if "-" in signs[i] or "+" in signs[i]:
                    signs[i] = self.determine_operator(signs[i])
        return signs

    def postfix_infix(self, infix):
        postfix = []
        stack = []
        priority = {"^": 3, "*": 2, "/": 2, "+": 1, "-": 1}
        for i in infix:
            if type(i) == int:
                postfix.append(i)
            elif i in self.variables:
                postfix.append(self.variables[i])
            else:
                if i == "(":
                    stack.append(i)
                elif i == ")":
                    operator = stack.pop()
                    while operator != "(":
                        postfix.append(operator)
                        operator = stack.pop()
                else:
                    while stack and stack[-1] in "^+-/*" and priority[i] <= priority[stack[-1]]:
                        postfix.append(stack.pop())
                    stack.append(i)
        while len(stack) != 0:
            postfix.append(stack.pop())
        return postfix

    def calculate_result(self, operation):
        operation = self.construct_math_operation(operation)
        postfix = self.postfix_infix(operation)
        stack = []
        result = 0
        if len(postfix) == 1:
            return postfix[0]
        else:
            for i in postfix:
                if type(i) == int:
                    stack.append(i)
                elif i in self.variables:
                    stack.append(self.variables[i])
                else:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    if i == "-":
                       result = num2 - num1
                    elif i == "+":
                        result = num1 + num2
                    elif i == "/":
                        result = num2 / num1
                    elif i == "*":
                        result = num1 * num2
                    elif i == "^":
                        result = num1**num2
                    stack.append(result)
            return int(result)



