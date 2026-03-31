class Solution:
    
    #isnt log(m * n) = log(m) + log(n)?
    #easy, just do two BS. One over the row and then over all the cols in that row.

    def row_bs(self, l, r, matrix, target) -> int:

        m,n = len(matrix), len(matrix[0])

        if l > r:
            return -1
        
        mid = (l + r) // 2

        if matrix[mid][0] <= target <= matrix[mid][n-1]:
            return mid
        elif target > matrix[mid][n-1]:
            return self.row_bs(mid + 1, r, matrix, target)
        else:
            return self.row_bs(l, mid -1, matrix, target)
    
    def bs(self, l, r, matrix, target, row) -> bool:

        if l > r:
            return False
        
        mid = (r + l) // 2

        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] > target:
            return self.bs(l, mid-1, matrix, target, row)
        else:
            return self.bs(mid+1, r, matrix, target, row)



    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #first find the row
        m,n = len(matrix), len(matrix[0])

        row = self.row_bs(0, m-1, matrix, target) # O(log(m))

        if row != -1:
            return self.bs(0, n-1, matrix, target, row) # O(log(n))
        else:
            return False