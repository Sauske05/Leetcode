import math
from typing import List
'''
This approach uses Binary Search to determine the **minimum eating speed (k)** such that Koko can finish all the bananas in `h` hours.

Problem Insight:
- Koko can choose an integer speed `k`, and at each hour eats up to `k` bananas from a single pile.
- For each pile, the time it takes is `ceil(pile / k)` hours.
- We need to **minimize k** such that the total time spent is at most `h` hours.

Binary Search Strategy:
- The smallest possible speed is 1 (slowest) and the largest is max(piles) (fastest, can finish any pile in 1 hour).
- We perform binary search between 1 and max(piles):
  - For a given mid value (candidate speed), compute total hours required with that speed.
  - If total hours > h → we are too slow → increase speed (`lp = mid + 1`).
  - Else → we might be able to eat slower → try lower speed (`rp = mid`).

The loop ends when lp == rp, which is the minimum valid speed that allows completion within `h` hours.

--> Time Complexity

Let n = number of piles, and m = max(piles)

- Binary Search Range: log(m)
- For each candidate speed, we calculate time with O(n) loop (or sum with ceil)

Total Time Complexity: O(n * log m)

--> Space Complexity

- The solution uses constant extra space except the temporary list from the list comprehension (can be optimized out if needed).

Total Space Complexity: O(1) auxiliary (O(n) if considering the list comprehension, but often ignored in complexity analysis)

'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h <= len(piles):
            return max(piles)

        lp, rp = 1, max(piles)
        while rp > lp:
            mid = (lp + rp) // 2
            #hours_spend = 0
            hours_spend = sum([math.ceil(pile/mid) for pile in piles])
            if hours_spend > h:
                lp = mid +1
            else:
                rp = mid
        return lp
        