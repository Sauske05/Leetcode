from collections import Counter, defaultdict
'''
This sliding window approach finds the minimum window substring in `s` that contains all characters from `t`, including duplicates.

--> Logic

1. Use `Counter(t)` to build a frequency map (`t_count`) of characters needed.
2. Initialize two pointers, `lp` and `rp`, to represent the sliding window.
3. Use a `window_count` dictionary to track character frequencies in the current window.
4. Track how many characters meet the required frequency using `have_count`. The goal is to match `need_count`, the number of unique characters in `t`.
5. Expand the window by moving `rp` to the right. For each character at `rp`:
   - If it's in `t_count`, update `window_count`.
   - If the frequency matches `t_count`, increment `have_count`.
6. Once `have_count` equals `need_count` (i.e., the window is valid), try to shrink the window from the left (`lp`) while keeping it valid.
   - Update the minimum window if the current one is smaller.
   - Shrink from the left, adjusting counts and possibly reducing `have_count` if a needed character falls below its required count.
7. Return the substring between indices `l` and `r` if a valid window was found; otherwise, return an empty string.

--> Time Complexity

- Building `t_count` using `Counter`: O(m), where m = len(t).
- Sliding Window:
   - Each character in `s` is visited at most twice (once by `rp`, once by `lp`): O(n), where n = len(s).
   - All dictionary operations are O(1) since the alphabet size is limited (usually 128 or 256 characters).

Total Time Complexity: O(n + m)

--> Space Complexity

- `t_count` and `window_count`: O(m), where m is the number of unique characters in `t`.
- Other variables use constant space.

Total Space Complexity: O(m)
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        #window_count = Counter(s[:len(t)])
        need_count = len(t_count)
        have_count = 0
        lp = 0
        rp = 0
        l = -1
        r = -1
        #min_string = ''
        length = float('inf')
        #found = False
        window_count = defaultdict(int)
        while rp < len(s):
            # while lp <= rp and s[lp] not in t_count:
            #     lp +=1
                
            if s[rp] in t_count:
                #t_count[s[rp]] -=1
                window_count[s[rp]] +=1
                #count -=1
                if window_count[s[rp]] == t_count[s[rp]]:
                    have_count +=1

            while need_count == have_count:
                #found = True
                #min_string = s[lp:rp+1]
                if (lp-rp+1) < length:

                    length = rp - lp + 1
                    l = lp
                    r = rp
                
                if s[lp] in t_count:
                    window_count[s[lp]] -=1
                    if window_count[s[lp]] < t_count[s[lp]]:
                        have_count -=1
                lp +=1
            rp +=1
        return s[l:r+1] if length != float('inf') else ''
        
