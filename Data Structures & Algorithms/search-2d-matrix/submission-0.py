class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top_row, bot_row = 0, ROWS - 1
        while top_row <= bot_row:
            mid_row = (top_row + bot_row) // 2
            if target > matrix[mid_row][-1]:
                top_row = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot_row = mid_row - 1
            else:
                break

        if not (top_row <= bot_row):
            return False

        mid_row = (top_row + bot_row) // 2
        l,r = 0, COLS - 1
        while l <= r:
            mid = (l+r)//2
            if target > matrix[mid_row][mid]:
                l = mid + 1
            elif target < matrix[mid_row][mid]:
                r = mid - 1
            else:
                return True
        return False