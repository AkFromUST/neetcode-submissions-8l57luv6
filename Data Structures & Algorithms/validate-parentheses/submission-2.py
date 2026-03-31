class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"[":"]", "{":"}", "(":")"}
        stack = []
        for brack in s:
            if brack in brackets:
                print("Open bracket")
                stack.append(brack)
            elif brack not in brackets and len(stack) > 0:
                last_brack = stack[-1]
                if brackets[last_brack] != brack:
                    return False
                stack.pop()
            elif brack not in brackets and len(stack) == 0:
                return False
        if stack:
            return False
        else:
            return True
