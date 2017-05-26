import re
from math import floor, log10, pow
import pdb

from src.calcresponse import CalcResponse

# https://stackoverflow.com/questions/3410976/how-to-round-a-number-to-significant-figures-in-python
# from comment by Roy Hyunjin Han on first answer
round_to_n = lambda x, n: round(x, -int(floor(log10(x))) + (n - 1))

class Calc:
    def parse_calculation(eq: str):
        pattern = r'^[0-9\(\)\./\*\+\-\^]*$'
        result = None

        if not re.match(pattern, eq):
            return CalcResponse(result, "Failure - invalid calculation")

        for char in eq:
            if char == "^":
                print(type(char))
                index = eq.index(char)
                print(type(eq))
                num_before = get_num_before_index(index, eq)
                num_after = get_num_after_index(index, eq)
                replacement = eval("pow({0}, {1})".format(num_before,
                                                          num_after))
                eq = eq.replace("{0}{1}{2}".format(num_before, char, num_after), "{}".format(replacement))
                print("eq: " + eq)

                if "^" not in eq:
                    break

        result = round_to_n(eval(eq), 8)
        return CalcResponse(round_to_n(result, 8), "Success")


def get_num_before_index(index, eq):
    num = ""
    in_brackets = False
    num_brackets = 0
    for char in list(reversed(eq[:index])):
        if not re.match(r'^[+\-*/^]*$', char) or num_brackets > 0:
            if char == ")":
                num_brackets += 1
            elif char == "(":
                num_brackets -= 1
            num = char + num
        else:
            break
    print("num-before: " + num)
    print(type(num))
    return num


def get_num_after_index(index, eq):
    num = ""
    for char in list(eq[index+1:]):
        if not re.match(r'^[+\-*/^]*$', char):
            num += char
        else:
            break
    print("num-after: " + num)
    print(type(num))
    return num
