from typing import List
'''
This approach uses two pointers (`lp` and `rp`) to find the maximum profit 
from a single buy-sell transaction in a list of stock prices.

We maintain a left pointer `lp` at the position of the minimum value seen so far, 
and a right pointer `rp` which scans forward through the array.

At each step:
- If the price at `rp` is lower than the price at `lp`, we move `lp` forward to `rp`,
  since we found a lower buying price.
- Otherwise, we compute the difference (potential profit) and update `max_diff` 
  if this difference is greater than the current `max_diff`.

--> Time Complexity

The loop runs once over the array: O(n), where n is the number of days/prices.
- Although there's a while loop inside the for loop, in practice `lp` only moves forward 
  and each element is visited at most once. Therefore, the total number of operations remains linear.

Total Time Complexity: O(n)

--> Space Complexity

We use a constant number of variables (`lp`, `rp`, `max_diff`), 
and no extra data structures.

Total Space Complexity: O(1)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp = 0
        max_diff = 0
        for rp in range(len(prices)):
            while prices[rp] < prices[lp]:
                lp +=1
            
            max_diff = max(max_diff, prices[rp] - prices[lp])
        return max_diff