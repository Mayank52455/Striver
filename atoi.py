class Solution:
    def myAtoi(self, s: str):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        def parse_number(index, current_number, is_negative):
            if index >= len(s) or not s[index].isdigit():
                return -current_number if is_negative else current_number

            current_number = current_number * 10 + int(s[index])

            if not is_negative and current_number > INT_MAX:
                return INT_MAX
            if is_negative and -current_number < INT_MIN:
                return INT_MIN

            return parse_number(index + 1, current_number, is_negative)

        i = 0
        n = len(s)

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Check sign
        is_negative = False
        if i < n and (s[i] == '-' or s[i] == '+'):
            is_negative = s[i] == '-'
            i += 1

        result = parse_number(i, 0, is_negative)
        return result
