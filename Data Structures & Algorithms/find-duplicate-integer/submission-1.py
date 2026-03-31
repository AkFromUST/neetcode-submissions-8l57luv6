class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        stack = []

        for n in nums:
            if (n not in stack):
                stack.append(n)
            else:
                return n
        