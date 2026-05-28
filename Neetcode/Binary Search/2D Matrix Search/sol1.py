class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        flat = []
        for i in matrix:
            flat.extend(i)
        
        l,r = 0, len(flat)-1

        while l <= r:
            mid = l + (r-l)//2
            if target == flat[mid]:
                return True
            if target > flat[mid]:
                l = mid+1
            else:
                r = mid-1
        
        return False
    
#scamming it lol
#O(n*m) space complexity, gotta reduce it down to O(1)