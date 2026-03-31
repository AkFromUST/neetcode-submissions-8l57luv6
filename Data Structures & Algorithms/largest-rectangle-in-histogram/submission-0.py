class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest, n = 0, len(heights)
        for i in range(n):
            local_largest = heights[i]
            for j in range(n):
                if i == j:
                    continue

                if i > j:
                    if heights[i] > heights[j]:
                        local_largest = heights[i]
                        continue
                
                if heights[i] <= heights[j]:
                    local_largest += heights[i]
                else:
                    break
            largest = max(largest, local_largest)
            print(heights[i], local_largest)
        return largest