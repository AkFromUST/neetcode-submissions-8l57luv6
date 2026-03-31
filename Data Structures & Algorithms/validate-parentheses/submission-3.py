class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"[":"]", "{":"}", "(":")"}
        stack = []
        for brack in s:
            if brack in brackets:
                stack.append(brack)
            elif brack not in brackets and len(stack) > 0:
                if brackets[stack.pop()] != brack:
                    return False
            elif brack not in brackets and len(stack) == 0:
                return False
        if stack:
            return False
        else:
            return True
