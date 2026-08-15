class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix)

        for i in range(n):
            found = self.bs(matrix[i], target)
            if found:
                return found
        return False

    
    def bs(self, arr, target):

        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if target < arr[mid]:
                right = mid - 1
            elif target > arr[mid]:
                left = mid + 1
            else:
                return True
        return False