class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        res = []
        cur =''
        for char in s:
            if char == '(' or char == '[' or char == '{':
                res.append(char)
            else:
                if res:
                    cur = res.pop()
                    if cur == '(' and char != ')':
                        return False
                    if cur == '{' and char != '}':
                        return False
                    if cur == '[' and char != ']':
                        return False
                else:
                    return False

        if res:
                return False
        return True