class Solution(object):
    def removeOuterParentheses(self, s):
        result = []
        bal = 0
        start = 0
        for i, char in enumerate(s):
            if char == '(':
                if bal = 0:
                    start = i
                bal += 1
            elif char == ')':
                bal -=1
                if bal == 0:
                    result.apend(s[start+1 : i])
        return"".join(result)
                

        
