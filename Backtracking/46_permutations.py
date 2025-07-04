from typing import List

'''
This solution generates all possible permutations of the list `nums` using backtracking.

# Approach: Backtracking with usage tracking (boolean `used` array)

--> Time Complexity
O(n * n!), where:
- n! = total number of permutations for list of length n
- Each of the n! permutations takes O(n) time to construct and append to the result

--> Space Complexity
O(n) for recursion stack + O(n!) * O(n) for the result list

Key Details:
- `path` is a list that grows as we build up each permutation
- `used` is a boolean array that keeps track of which elements in `nums` have been used in the current path
- If an element is already used, it is skipped
- Once `path` has all n elements, it is added to `result`
- After the recursive call, the last element is removed (`path.pop()`), and the corresponding `used[i]` is reset

This is a clean and efficient way to generate all permutations without modifying the original input array.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtrack(used):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(used)
                    path.pop()
                    used[i] = False

        backtrack([False] * len(nums))
        return result
