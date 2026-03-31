class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        #case 1: more than 1 zero
        count_zero = 0
        for num in nums:
            if num == 0:
                count_zero += 1

        totalProd = 1
        output = []
        if count_zero == 1:
            for num in nums:
                if num == 0:
                    continue
                totalProd *= num
            for num in nums:
                if num != 0:
                    output.append(0)
                else:
                    output.append(totalProd)
            return output
        
        if count_zero > 1:
            for num in nums:
                output.append(0)
            return output

        #case 2: no zeroes
        if count_zero == 0:
            for num in nums:
                totalProd *= num
        
        for i in range(len(nums)):
            result = 1 
            if (nums[i] != 0):
                result = int(totalProd / nums[i])
            else:
                result = totalProd
            output.append(result)
        return output 