from typing import List

'''
This solution finds all unique combinations in `candidates` where the numbers sum up to `target`.
Each number in `candidates` may be used an unlimited number of times.

# First Solution: Uses a set to avoid duplicate combinations (by sorting paths)

--> Time Complexity
O(2^t * k), where:
- t = target value
- k = average length of a valid combination
- The recursion explores multiple paths, and sorting each combination adds overhead

--> Space Complexity
O(k) for recursion stack + O(#unique_combinations * k) for result set

Key Details:
- `backtrack(sum_)` explores all possible combinations recursively
- Paths are sorted and stored as tuples in a set to eliminate duplicates
- Sorting each path adds extra computation
- This version doesn't control traversal order via index, so duplicates are manually handled using the set

'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.output = set()
        self.path = []

        def backtrack(sum_):
            if sum_ <= 0:
                if sum_ == 0:
                    sorted_path = tuple(sorted(self.path[:]))
                    self.output.add(sorted_path)
                return

            for num in candidates:
                self.path.append(num)
                backtrack(sum_ - num)
                self.path.pop()

        backtrack(target)
        return [list(tup) for tup in self.output]



'''
# Second Solution: Uses start index to control combination generation and naturally avoid duplicates

--> Time Complexity
O(2^t * k), similar to the first solution:
- Recursion depth varies with target value
- No path sorting is needed, so it's slightly faster in practice

--> Space Complexity
O(k) for recursion stack + O(#valid_combinations * k) for result list

Key Details:
- `backtrack(start, sum_)` ensures that combinations are generated in a non-decreasing order
- This naturally avoids duplicates without needing a set or sorting
- The same element can be reused (`backtrack(i, ...)`)
- Cleaner and more efficient for combination-type problems

This version is the standard and preferred approach for problems like Combination Sum due to its efficiency and elegance.
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.output = []
        self.path = []

        def backtrack(start, sum_):
            if sum_ <= 0:
                if sum_ == 0:
                    self.output.append(self.path[:])
                return

            for i in range(start, len(candidates)):
                self.path.append(candidates[i])
                backtrack(i, sum_ - candidates[i])
                self.path.pop()

        backtrack(0, target)
        return self.output
