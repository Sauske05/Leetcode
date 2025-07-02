from typing import List
'''
This approach generates all possible subsets (the power set) of a given list of integers using Depth-First Search (DFS) with backtracking.

--> Time Complexity
O(2^n), where n is the length of nums:
- Each element has two choices: include or exclude
- Total of 2^n subsets generated

--> Space Complexity
O(n) for the recursive call stack:
- The depth of the recursion tree is at most n
- Temporary space for storing subsets during backtracking

Key Details:
- A DFS helper function explores two branches at each index: 
  1. Include the current element in the subset
  2. Exclude the current element
- A shallow copy (`self.subset[:]`) is appended to the result to avoid reference issues
- Backtracking is used to undo choices (via `pop()`) and explore alternate paths
- The recursion ends when the index exceeds the length of the input list

This solution is efficient and ensures that all subset combinations are explored without duplication.
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.subset = []

        def dfs(i):
            #Base Case
            if i >= len(nums):
                self.result.append(self.subset[:]) #Shallow copy
                return

            #Right Case
            self.subset.append(nums[i])
            dfs(i+1)
            
            #left Case
            self.subset.pop()
            dfs(i+1)


        dfs(0)

        return self.result