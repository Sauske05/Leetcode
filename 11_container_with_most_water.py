from typing import List

"""
This is the optimal two-pointer solution to the 'Container With Most Water' problem.

--> Time Complexity
The algorithm runs in O(n) time:
- Only a single pass is needed where two pointers (left and right) move toward each other.

--> Space Complexity
O(1) space:
- No additional space is used apart from a few variables.


This approach is optimal. It starts with the widest container (ends of the array) and 
moves the pointer pointing to the shorter line inward to potentially find a taller line.
This ensures we explore all possible maximum areas efficiently without checking every pair.
An additional conditional handles the rare case of equal heights by trying to skip 
toward a potentially taller line. This extra heuristic is optional but safe.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        lp = 0
        rp = len(height) - 1

        while rp > lp:
            min_height = min(height[rp], height[lp])
            max_area = max(min_height * (rp - lp), max_area)

            if height[rp] > height[lp]:
                lp += 1
            elif height[rp] < height[lp]:
                rp -= 1
            elif height[rp] == height[lp]:
                if height[rp - 1] > height[rp]:
                    rp -= 1
                else:
                    lp += 1

        return max_area
