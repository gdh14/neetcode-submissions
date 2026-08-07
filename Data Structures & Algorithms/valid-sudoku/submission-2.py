""" 
Straigh forward idea, just check by row, column and 3x3 grid using hashset.

Caveat: iterate the 3x3 grid is a bit tricky with the index
Kudos: I solved it correctly on my own!!
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # verify each row
        for row_id in range(9):
            row = board[row_id]
            temp_set = set()
            for num in row:
                if num in temp_set:
                    return False
                elif num != '.':
                    temp_set.add(num)

        # verify each column
        for col_id in range(9):
            col = [board[i][col_id] for i in range(9)]
            temp_set = set()
            for num in col:
                if num in temp_set:
                    return False
                elif num != '.':
                    temp_set.add(num)

        # verify each 3x3 grid
        for i in range(0, 9, 3): 
            for j in range(0, 9, 3):
                temp_set = set()
                for m in range(3):
                    for n in range(3):
                        num = board[i + m][j + n]
                        if num in temp_set:
                            return False
                        elif num != '.':
                            temp_set.add(num)

        return True        