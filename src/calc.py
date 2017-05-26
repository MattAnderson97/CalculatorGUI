import re
from math import floor, log10

from calcresponse import CalcResponse

# https://stackoverflow.com/questions/3410976/how-to-round-a-number-to-significant-figures-in-python
# from comment by Roy Hyunjin Han on first answer
round_to_n = lambda x, n: round(x, -int(floor(log10(x))) + (n - 1))

class Calc:
    @staticmethod
    def parse_calculation(calc):
        pattern = r'^[0-9\(\)\./\*\+\-]*$'
        result = None
        valid = True
        for char in calc:
            if not re.match(pattern, char):
                valid = False
                break
        if valid:
            result = round_to_n(eval(calc), 8)
            return CalcResponse(result, "Success")
        else:
            return CalcResponse(result, "Failure - invalid calculation")
