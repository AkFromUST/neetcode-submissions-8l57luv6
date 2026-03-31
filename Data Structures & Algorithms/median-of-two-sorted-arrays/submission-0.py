class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        res_arr = []

        for element in nums1:
            res_arr.append(element)
        
        for element in nums2:
            res_arr.append(element)
        
        res_arr.sort()

        if len(res_arr) % 2 == 0:
            mid = (len(res_arr) - 1) // 2
            return (res_arr[mid] + res_arr[mid + 1]) / 2
        else:
            mid = (len(res_arr) - 1) // 2
            return (res_arr[mid])