class Solution(object):
    def myAtoi(self, s):
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        def parse_number(index, current_num, is_negative):
            if index >= len(s) or not s[index].isdigit():
                return -current_num if is_negative else current_num

            current_num = current_num * 10 + int(s[index])

            if not is_negative and current_num > INT_MAX:
                return INT_MAX
            if is_negative and -current_num < INT_MIN:
                return INT_MIN

            return parse_number(index + 1, current_num, is_negative)

        i = 0
        n = len(s)

        # skip spaces
        while i < n and s[i] == ' ':
            i += 1

        # check sign
        is_negative = False
        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                is_negative = True
            i += 1

        return parse_number(i, 0, is_negative)
