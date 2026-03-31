class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
            
        #I completely forgot about the K thing. Hahahaha. This makes it easy. Dynamic Sliding Window

        #first check
        state = set()

        n = len(nums)
        if n <= 1:
            return False

        upto = min(k,n)
        for i in range(upto):
            ch = nums[i]
            if ch not in state:
                state.add(ch)
            else:
                return True

        if k == 0:
            return False

        l = 0
        for i in range(upto, n):
            if nums[i] in state:
                return True
            state.remove(nums[l])
            state.add(nums[i])
            l += 1
        return False