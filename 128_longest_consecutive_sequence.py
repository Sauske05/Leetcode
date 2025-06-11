from typing import List
'''
This approach identifies the longest consecutive sequence by expanding each number in both directions (forward and backward)
to form a consecutive set. It keeps track of the largest such set found so far.

The algorithm uses a hash set (`hash_set`) for O(1) lookups, and iterates over each number in `nums`. For each number:

- If it is already part of a previously found sequence (`longest_seq`), we skip it.
- Otherwise, we try to expand the sequence in both the decreasing (`num - 1`) and increasing (`num + 1`) directions.
- We keep the largest sequence found in `longest_seq` and return its length.

This was the **first approach that came to mind**, and while it works correctly, there is a slightly more **optimal solution** 
that avoids constructing intermediate sets and instead looks only for the beginning of sequences, resulting in better efficiency.

--> Time Complexity

- In the worst case, for each number, we might re-check previously visited elements when expanding the sequence.
- In practice, the use of `longest_seq` avoids recomputation for overlapping elements.
- Still, the repeated lookups and `set` operations can cause inefficiencies.

Total Time Complexity: Approximately O(n^2) in the worst case due to nested `while` loops and multiple `set` operations.

--> Space Complexity

- `hash_set` takes O(n) space for storing unique elements.
- `longest_seq` and `temp` are sets used for temporary storage of sequences; their maximum size is O(n) in worst case.

Total Space Complexity: O(n) due to the sets used.

--> Note

There exists a more optimal O(n) solution that checks only for the start of sequences:
For each number, if `num - 1` is **not** in the set, it means this could be the start of a new sequence. 
Then we only move forward (`num + 1`, `num + 2`, ...) and count the length of that sequence.

That avoids redundant checks and doesn't require storing each sequence explicitly.
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hash_set = set(nums)
        longest_seq = set([])
        for num in nums:
            if num in longest_seq:
                continue
            temp = set()
            temp.add(num)
            while num-1 in hash_set:
                temp.add(num-1)
                num = num - 1
            while num+1 in hash_set:
                temp.add(num+1)
                num += 1
            if len(longest_seq) < len(temp):
                longest_seq = temp

        return len(longest_seq)
            