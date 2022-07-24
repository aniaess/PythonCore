class Regex:
    special_char = ["^", ".", "*", "?", "+"]

    def __init__(self, pattern, word):
        self.regex = pattern
        self.word = word
        print(self.regex_engine(self.regex, self.word))

    @staticmethod
    def special_cases(pattern, word):
        if pattern[1] == "*" or pattern[1] == "?":
            return True
        elif pattern[1] == "+" and len(word) >= 1:
            return True
        else:
            return False

    def dot_special_char(self, pattern, word): #np .*
        if pattern[1] == "?":
            if pattern[2] == word[0]:
                return self.regex_engine(pattern[3:], word[2:], True)
            else:
                return self.regex_engine(pattern[2:], word[1:], True)
        else:
            if pattern[1] == "*":
                indeks = len(word) - word[::-1].find(pattern[2])
                if indeks == -1:
                    return False
                else:
                    return self.regex_engine(pattern[3:], word[indeks + 1:], True)
            else:
                if len(word) > 2:
                    indeks = len(word[1:]) - word[1:][::-1].find(pattern[2])
                    if indeks == -1:
                        return False
                    else:
                        return self.regex_engine(pattern[3:], word[indeks + 1:], True)
                else:
                    return False

    def regular_char_special_char(self, pattern, word):
        if pattern[0] == word[0]:
            if pattern[1] == "?":
                return self.regex_engine(pattern[2:], word[1:], True)
            elif pattern[1] == "*" or pattern[1] == "+":
                indeks = [word.find(i) for i in word if i != pattern[0]][0]
                return self.regex_engine(pattern[2:], word[indeks:], True)
        else:
            if pattern[1] == "?" or pattern[1] == "*":
                return self.regex_engine(pattern[2:], word, True)
            else:
                return False

    def special_characters(self, pattern, word):
        if pattern[0] == "^":
            if '^' == pattern:
                return True
            elif pattern[1] == word[0]:
                # print(pattern, word)
                return self.regex_engine(pattern[2:], word[1:], True)
            else:
                if pattern[2] not in Regex.special_char:
                    return False
                else:
                    return self.regex_engine(pattern[1:], word)
        elif len(pattern) == 2 and pattern[0] == "." and pattern[1] in [ "*", "?", "+"]:
            return Regex.special_cases(pattern, word)
        elif len(pattern) > 1 and pattern[1] in ["+", "*", "+", "?"]:
            if pattern[0] == "." and len(pattern) >2:
                return self.dot_special_char(pattern, word)
            else: #gdy nie ma kropki przed znakiem specjalnym
                return self.regular_char_special_char(pattern, word)
        else:
            return self.regex_engine(pattern[1:], word[1:])

    @staticmethod
    def termination(pattern,word):
        if not pattern:
            return True
        if not word:
            if pattern == '$':
                return True
            elif pattern == "^":
                return True
            else:
                return False

# flag= False (not restricted searching) searching for first matching character in word
#       True - means if we find first matching characters next characters must also match
    def regex_engine(self, pattern, word, flag=False):
        # print(pattern, word)
        if not pattern or not word:
            return Regex.termination(pattern, word)
        elif pattern[0] == "\\":
            return self.regex_engine(pattern[1:], word)
        elif pattern[0] in Regex.special_char:
            # print(pattern[0])
            return self.special_characters(pattern, word)
        elif len(pattern) > 1 and pattern[1] in ["^", "*", "?", "+"]: # gdy pattern ma znak specjalny po literze
            return self.special_characters(pattern, word)
        else:
            if pattern[0] == word[0]:
                return self.regex_engine(pattern[1:], word[1:], True)
            else:
                if flag:
                    if self.regex[0] == "^":
                        return False
                    else:
                        pattern = self.regex
                        return self.regex_engine(pattern, word[1:])
                else:
                    return self.regex_engine(pattern, word[1:], flag)


pattern, word = tuple(input().split("|"))
regex_machine = Regex(pattern, word)
