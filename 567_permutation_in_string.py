from collections import Counter
'''
This approach checks whether one string (`s1`) is a permutation of a substring in another string (`s2`) using a sliding window and frequency maps.

Core Logic:
- Use a fixed-size sliding window of length `len(s1)` across `s2`.
- Maintain character frequency maps (`Counter`) for `s1` and the current window in `s2`.
- If the two frequency maps match at any point, it means a permutation of `s1` exists in `s2`.

--> Time Complexity

Initial Counter Creation:
- Building `count_s1` takes O(k), where k = len(s1).
- Building `count_s2` for the first window takes O(k).

Sliding Window:
- The loop runs (n - k) times, where n = len(s2).
- Each iteration involves:
    - Incrementing the count of the new character entering the window.
    - Decrementing the count of the character exiting the window.
    - Comparing two Counter objects (which takes O(26) = O(1) time due to fixed lowercase alphabet size).

Total Time Complexity: O(k) + O(n - k) * O(1) = O(n), where n = len(s2) and k = len(s1).

--> Space Complexity

Counter Objects:
- `count_s1` and `count_s2` store at most 26 lowercase letters.
- Space used is O(1) due to the fixed alphabet size.

Total Space Complexity: O(1)
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_s1 = Counter(s1)
        count_s2 = Counter(s2[:len(s1)])

        if count_s1 == count_s2:
            return True

        for rp in range(len(s1), len(s2)):
            count_s2[s2[rp]] +=1
            count_s2[s2[rp - len(s1)]] -=1

            if count_s1 == count_s2:
                return True
        
        return False 