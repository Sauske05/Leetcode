'''
This approach solves the problem of finding the length of the longest substring where
we can replace at most `k` characters to make all characters in the substring the same.

We use a **sliding window** approach with two pointers (`lp` and `rp`) and a dictionary
`char_count` to keep track of character frequencies within the current window.

Key idea:
- For each window [lp, rp], we track the count of the most frequent character (`frequent_count`).
- The number of characters that need replacement is (window size - frequent_count).
- If this number exceeds `k`, we shrink the window from the left (increment `lp`).
- Otherwise, we keep expanding the window and update the `max_count` (maximum valid window size).

--> Time Complexity

- The `rp` pointer moves from 0 to n-1 => O(n)
- Each character is added/removed from the count map in constant time => O(1)
- Finding `frequent_count` using `max()` on all values takes O(26) at most (uppercase English letters), which is constant.

Total Time Complexity: O(n), where n is the length of the string.

--> Space Complexity

- `char_count` dictionary stores up to 26 entries for uppercase English letters.

Total Space Complexity: O(1)
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lp = 0
        max_count = 0
        char_count = {k:0 for k in set(s)}
        for rp in range(len(s)):
            char_count[s[rp]] +=1
            frequent_count = max([val for val in char_count.values()])
            
            if rp - lp + 1 - frequent_count >k:
                char_count[s[lp]] -=1
                lp +=1

            max_count = max(max_count, rp - lp+1)
            
        return max_count
