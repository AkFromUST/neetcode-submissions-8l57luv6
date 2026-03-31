class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while (i < j):
            x_sum = numbers[i] + numbers[j]

            if (target == x_sum):
                return [i+1, j+1]
            elif (target > x_sum):
                i += 1
            else:
                j -= 1
        