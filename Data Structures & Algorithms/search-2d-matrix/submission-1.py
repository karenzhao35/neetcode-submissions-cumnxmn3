class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix)-1
        mid = 0 
        while lo <= hi: 
            mid = (lo+hi)//2
            val = matrix[mid][0]
            if target == val: return True
            if target > val: 
                lo = mid+1
            else: 
                hi = mid-1
        

        m = lo-1
        lo, hi = 0, len(matrix[0])-1
        while lo <= hi: 
            mid = (lo+hi)//2
            val = matrix[m][mid]
            if target == val: return True
            if target > val: 
                lo = mid+1
            else: 
                hi = mid-1

        return False
