class InvalidAssigment(Exception):
    def __str__(self):
        return "Invalid assigment"

class InvalidIdentifier(Exception):
    def __str__(self):
        return "Invalid identifier"

class InvalidExpression(Exception):
    def __str__(self):
        return "Invalid expression"

class UnknownVariable(Exception):
    def __str__(self):
        return "Unknown variable"