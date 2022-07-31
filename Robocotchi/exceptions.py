class MoreThanMilionError(Exception):
    def __str__(self):
        return "Invalid input! The number can't be bigger than 1000000"

class LessThanZeroError(Exception):
    def __str__(self):
        return "The number can't be negative!"
