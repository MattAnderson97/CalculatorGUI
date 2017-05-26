import re

from calcresponse import CalcResponse


class Calc:
    @staticmethod
    def parse_calculation(calc):
        pattern = r'^[0-9\(\)\./\*\+\-]*$'
        result = 0
        valid = True
        for char in calc:
            if not re.match(pattern, char):
                valid = False
                break
        if valid:
            result = eval(calc)
            return CalcResponse(result, "Success")
        else:
            return CalcResponse(result, "Failure - invalid calculation")
