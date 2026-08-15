class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        item_possible_position = None

        top_row, bot_row = 0, ROWS - 1
        while top_row <= bot_row:
            mid_row = (top_row + bot_row) // 2
            if target > matrix[mid_row][-1]:
                top_row = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot_row = mid_row - 1
            else:
                item_possible_position = mid_row
                break

        if top_row > bot_row:
            return False

        l,r = 0, COLS - 1
        while l <= r:
            mid = (l+r)//2
            if target > matrix[item_possible_position][mid]:
                l = mid + 1
            elif target < matrix[item_possible_position][mid]:
                r = mid - 1
            else:
                return True
        return False