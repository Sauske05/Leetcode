from typing import List
'''
This approach uses backtracking to generate all valid combinations of well-formed parentheses.

Key Idea:
- Use a recursive backtrack function to explore all possible placements of '(' and ')'.
- Track how many opening (`open_`) and closing (`close_`) brackets have been added so far.
- Only add '(' if `open_ <= n` (to stay within limit), and only add ')' if `close_ < open_` (to maintain validity).
- Once a valid string of length `2 * n` is formed, add it to the result.

Note:
- The initial call starts with `backtrack(1, 1)`,

--> Time Complexity

Each recursive call makes up to two further calls.
- In the worst case, there are Catalan number C(n) valid combinations.
- Time Complexity: O(4^n / sqrt(n)), which is the complexity of generating all valid combinations of parentheses of length 2n.

--> Space Complexity

- The recursion depth can go up to 2n → O(n).
- The output list stores all valid combinations → O(2^n) in worst case due to exponential number of strings.

Total Space Complexity: O(n) for the call stack, O(C(n)) for the output.

'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        snapshot, output = [], []
        def backtrack(open_, close_):
            if len(snapshot) == 2 * n:
                output.append(''.join(snapshot))
                return
            
            #Add '('
            if open_ <=n:
                snapshot.append('(')
                backtrack(open_+1, close_)
                snapshot.pop()
            #Add ')'
            if close_ < open_:
                snapshot.append(')')
                backtrack(open_, close_+1)
                snapshot.pop()
        backtrack(1,1)
        return output
             
