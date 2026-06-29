class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l,r = 0, n-1

        while l < r:
            c = numbers[l] + numbers[r]
            if c < target:
                l += 1
            if c > target:
                r -= 1
            if c == target:
                return [l+1,r+1]