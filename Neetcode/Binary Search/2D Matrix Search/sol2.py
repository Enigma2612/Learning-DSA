class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l1, r1 = 0, len(matrix) - 1

        row = 0
        while l1 <= r1:
            mid = l1 + (r1 - l1)//2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                row = mid
                l1 = mid + 1
            else:
                r1 = mid - 1

        l2, r2 = 0, len(matrix[row])-1

        while l2 <= r2:
            mid = l2 + (r2 - l2)//2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l2 = mid + 1
            else:
                r2 = mid - 1
        return False
    

#non scam solution
#O(log(n*m)) time, O(1) space