class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #O(1) kind of gives us the hint that we need to use two pointers.
        #luckily, the input array is sorted


        i,j = 0, len(numbers)-1

        while i <= j:
            pointerSum = numbers[i] + numbers[j]
            if (pointerSum == target):
                return [i+1,j+1]
            elif pointerSum < target:
                i += 1
            else:
                j -= 1
        