from typing import List
'''
This approach treats the 2D matrix as a virtual 1D sorted array and applies binary search.

Since each row is sorted left to right and the first integer of each row is greater than the last integer of the previous row,
we can flatten the matrix conceptually into a single sorted list of size rows * cols.

To perform binary search:
- We initialize `lp` (left pointer) to 0 and `rp` (right pointer) to rows * cols - 1.
- In each iteration, we calculate the middle index `mid`.
- We convert `mid` back into 2D indices using `divmod(mid, cols)` to get the corresponding `row` and `col`.
- We compare the matrix value at that position with the target:
  - If greater, move the search space to the left half (`rp = mid - 1`).
  - If smaller, move to the right half (`lp = mid + 1`).
  - If equal, we return True as the target exists.

If the loop ends without a match, we return False.

--> Time Complexity

Each iteration cuts the search space in half → O(log (rows * cols))

Let n = total elements = rows * cols

Total Time Complexity: O(log n)

--> Space Complexity

Only a constant amount of space is used for pointers and intermediate variables.

Total Space Complexity: O(1)
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        lp, rp = 0, rows*cols - 1
        while rp >= lp:
            mid = (lp + rp) // 2
            row, col = divmod(mid, cols)
            if matrix[row][col] > target:
                rp = mid- 1
            elif matrix[row][col] < target:
                lp = mid + 1
            else:
                return True
        return False
