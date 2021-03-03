from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in board:
            for col in row:
                if col != "." and col in seen:
                    print("False row at ", row, col)
                    return False
                seen.add(col)
            seen.clear()

        for row in range(9):
            for col in range(9):
                if board[col][row] != "." and board[col][row] in seen:
                    print("False col at ", row, col)
                    return False
                seen.add(board[col][row])
            seen.clear()
        start_row = 0
        start_col = 0

        while start_row != 9:
            for row in range(start_row, start_row+3):
                for col in range(start_col, start_col + 3):
                    if board[row][col] != "." and board[row][col] in seen:
                        print("False sq at ", row, col)
                        return False
                    seen.add(board[row][col])
            seen.clear()
            start_col +=3
            if start_col == 9:
                start_col = 0
                start_row +=3

        return True