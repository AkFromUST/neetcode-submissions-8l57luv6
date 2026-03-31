class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        #pretty easy. Use a Stack
        stack = []
        n = len(asteroids)

        for r in range(n):
            curr = asteroids[r]
            
            if not stack:
                stack.append(curr)
                continue

            last = stack[-1]

            #collision
            if last > 0 and curr < 0:
                if last + curr == 0:
                    stack.pop()
                    continue
                
                while stack and (stack[-1] > 0 and curr < 0) and abs(curr) > abs(stack[-1]):
                    stack.pop()
                
                if not stack or stack[-1] < 0:
                    stack.append(curr)
                    continue
                if stack[-1] == abs(curr):
                    stack.pop()
            else:
                stack.append(curr)

        return stack
