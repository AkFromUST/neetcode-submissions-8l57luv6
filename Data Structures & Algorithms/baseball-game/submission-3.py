class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        n = len(operations)

        for r in range(n):
            ops = operations[r]

            if ops == "+":
                temp1 = stack.pop()
                temp2 = stack.pop()
                new_score = temp1 + temp2

                stack.append(temp2)
                stack.append(temp1)
                stack.append(new_score)

            elif ops == "D":
                temp1 = stack.pop()
                new_score = temp1 * 2

                stack.append(temp1)
                stack.append(new_score)
            
            elif ops == "C":
                stack.pop()

            else:
                stack.append(int(ops))

        return sum(stack) if stack else 0