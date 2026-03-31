class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        curr_max = -1*float("inf")

        i, j = 0, len(heights)-1

        while i < j and i < len(heights) and j < len(heights):
            curr_max = max(curr_max, min(heights[i], heights[j]) * (j-i))
            print("evaluating\ti:", i, "\tj:", j, "\tCurrent max is:", curr_max)
            if (heights[i] > heights[j]):
                j -= 1
            elif heights[i] < heights[j]:
                i += 1
            else:
                i += 1
        return curr_max
            