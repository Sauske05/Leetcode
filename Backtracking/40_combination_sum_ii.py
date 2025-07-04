from typing import List
'''
This solution finds all unique combinations in `candidates` where the numbers sum to `target`.
Each number may only be used **once**, and the input may contain duplicates.

# Approach: Backtracking with sorted input and duplicate-skipping logic

--> Time Complexity
O(2^n), where:
- n = number of candidates
- Each element can either be included or excluded
- Pruning and duplicate checks reduce the actual number of calls

--> Space Complexity
O(k) for recursion stack + O(#valid_combinations * k) for result list

Key Details:
- Input is sorted to allow early stopping (`if candidates[i] > sum_`) and easy duplicate detection
- `backtrack(start, sum_)` builds valid combinations without reusing the same index
- Duplicates are skipped using `if i > start and candidates[i] == candidates[i-1]`
- Only `i+1` is passed to the recursive call to prevent reusing the same element
- Result is stored directly in `self.output` as a list of lists

This approach is particularly useful when:
- Input can contain duplicate elements
- Each number can only be used once in a combination
- You want to avoid returning duplicate combinations in the final result
'''

class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.output = []
        self.path= []
        def backtrack(start,sum_):
            if sum_ == 0:
                self.output.append(self.path[:])
            for i in range(start, len(candidates)):
                #Skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                if candidates[i] > sum_:
                    break

                self.path.append(candidates[i])
                backtrack(i+1, sum_ - candidates[i]) #no reuse
                self.path.pop()
        
        
        backtrack(0, target)
        return self.output