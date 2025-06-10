from typing import List

'''
This approach checks if a given 9x9 Sudoku board is valid.

A Sudoku board is valid if:
1. Each row contains the digits 1-9 at most once.
2. Each column contains the digits 1-9 at most once.
3. Each of the 3x3 subgrids (boxes) contains the digits 1-9 at most once.

Important Note:
Unlike NumPy arrays, Python lists do not support 2D slicing. So we cannot directly slice 3x3 subgrids
like `board[0:3, 0:3]`. Instead, we use nested loops to manually collect values from each 3x3 box.

Step-by-step:

1. Check all rows:
   - For each row, check that all digits (excluding '.') are unique.
2. Check all columns:
   - For each column index, collect the elements at that column from each row and check uniqueness.
3. Check all 3x3 subgrids:
   - There are 9 such subgrids. We use a step of 3 to iterate over the top-left cell of each subgrid
     and then check the 3x3 block starting at that cell using two nested loops.

--> Time Complexity

- Checking rows: O(9 × 9)
- Checking columns: O(9 × 9)
- Checking subgrids: O(9 × 9)
Each cell is visited exactly once per type of check.

Total Time Complexity: 3* O(81) = O(1), since 9x9 is constant size.

--> Space Complexity

- We use a set to track seen values in each row, column, or grid.
- The space for these sets is constant.

Total Space Complexity: O(1)
'''
class Solution:
    def row_col_val(self, slice_n:List[str]) -> bool:
        seen = set()
        for val in slice_n:
            if val!= '.':
                if val not in seen:
                    seen.add(val)
                else:
                    return False
        return True
    
    def valid_grid(self, board: List[List[str]], start_row:int, start_column:int) -> bool:
        seen = set()
        for grid_row in range(3):
            for grid_col in range(3):
                if board[start_row+ grid_row][start_column+grid_col]!= '.':
                    if board[start_row+ grid_row][start_column+grid_col] not in seen:
                        seen.add(board[start_row+ grid_row][start_column+grid_col])
                    else:
                        return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Row Wise
        for row in board:
            if not self.row_col_val(row): return False
        #Column Wise
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.row_col_val(column): return False
        #Grid Wise
        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                if not self.valid_grid(board,row, column): return False

        return True    
    