import re
from errors import InvalidIdentifier, InvalidAssigment, InvalidExpression, UnknownVariable

class ErrorHandler:
    pattern = r"([a-z]+\d+)|(\d+[a-z]+)"

    def __init__(self, regex):
        self.regex = regex

    def update_variables(self, variables):
        err = re.search(ErrorHandler.pattern, self.regex[-1])
        try:
            if len(self.regex) > 3:
                raise InvalidAssigment
            if self.regex[0].isalpha():
                if self.regex[-1].isalpha() and self.regex[-1] in variables:
                    variables[self.regex[0]] = variables[self.regex[-1]]
                elif err:
                    raise InvalidAssigment
                elif self.regex[-1] not in variables and self.regex[-1].isalpha():
                    raise UnknownVariable
                else:
                    variables[self.regex[0]] = int(self.regex[-1])
            else:
                raise InvalidIdentifier
        except InvalidAssigment as err:
            print(err)
        except InvalidIdentifier as err:
            print(err)
        except UnknownVariable as err:
            print(err)
        return variables

    def errors(self, variables):
        for i in range(len(self.regex)):
            err = re.search(ErrorHandler.pattern, self.regex[i])
            try:
                if err:
                    raise InvalidIdentifier
                if self.regex[i] not in variables and self.regex[i].isalpha():
                    raise UnknownVariable
                elif "*" in self.regex[i] or "/" in self.regex[i]:
                    if len(self.regex[i]) > 1:
                        raise InvalidExpression
            except InvalidExpression as err:
                print(err)
                return 1
            except UnknownVariable as err:
                print(err)
                return 1

    def error1(self, variables):
        if len(self.regex) == 2:
            try:
                if self.regex[-1] in ["-", "+"]:
                    raise InvalidExpression
                else:
                    try:
                        print(int("".join(self.regex)))
                    except ValueError:
                        v = str(variables[self.regex[-1]])
                        print(int("".join([self.regex[0],v])))
            except InvalidExpression as err:
                print(err)
            return 1

    def check_parethesis(self):
        parenthesis = []
        for i in self.regex:
            if i == "(":
                parenthesis.append(i)
            elif i == ")":
                try:
                    if parenthesis[-1] == "(":
                        parenthesis.pop()
                except IndexError:
                    parenthesis.append(")")
        try:
            if parenthesis:
                raise InvalidExpression
        except InvalidExpression as err:
            print(err)
            return 1