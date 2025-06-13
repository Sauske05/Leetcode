'''
This approach uses the **sliding window technique** with two pointers (`lp` and `rp`)
to find the length of the longest substring without repeating characters.

We use a set `seen` to keep track of characters currently in the window.

Algorithm:
- `lp` is the left pointer of the window.
- `rp` is the right pointer, iterating through the string.
- While the character at `rp` is already in `seen`, we shrink the window from the left
  by removing characters from `seen` and incrementing `lp` until the duplicate is removed.
- Then, we add the current character `s[rp]` to `seen`.
- At each step, we update `max_length` as the size of the current valid window.

--> Time Complexity

Each character is visited at most twice (once by `rp`, once by `lp`):
- Set operations (add, remove, and `in`) are O(1) on average.
- Total operations are linear in the size of the string.

Total Time Complexity: O(n), where n is the length of the string.

--> Space Complexity

The `seen` set stores at most n characters in the worst case (if all are unique).

Total Space Complexity: O(n)
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        lp = 0
        max_length = 0
        seen = set()
        for rp in range(len(s)):
            while s[rp] in seen:
                seen.remove(s[lp])
                lp +=1
            if not s[rp] in seen:
                seen.add(s[rp])
            max_length = max(max_length, len(seen))
        
        return max_length

