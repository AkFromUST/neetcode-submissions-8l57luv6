class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        nums = [-1*n for n in nums]
        heapq.heapify(nums)

        for i in range(k-1):
            heapq.heappop(nums)
        
        return -1 * nums[0]