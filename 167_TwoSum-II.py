
from typing import List
'''
This approach uses the two-pointer technique on a **sorted** list to efficiently find two numbers that sum up to the target. 
We initialize two pointers: `lp` at the beginning and `rp` at the end of the list. 
We then move them closer based on the current sum compared to the target:

- If the sum of numbers[lp] and numbers[rp] equals the target, we return the 1-based indices.
- If the sum is greater than the target, we move the right pointer left to reduce the sum.
- If the sum is less than the target, we move the left pointer right to increase the sum.

This works efficiently due to the sorted nature of the input array.

--> Time Complexity

- The while loop ensures that we examine each element at most once from either side.
- In the worst case, each pointer traverses the list once, resulting in O(n) time complexity.

Total Time Complexity: O(n), where n is the number of elements in `numbers`.

--> Space Complexity

- The algorithm uses only a few integer variables (`lp`, `rp`) and no extra data structures.

Total Space Complexity: O(1) – constant space.
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers) - 1
        while lp<=rp:
            if numbers[lp] + numbers[rp] == target:
                return [lp+1, rp+1]
            while numbers[lp] + numbers[rp] > target and lp < rp:
                rp -=1
            while numbers[lp] + numbers[rp] < target and lp < rp:
                lp +=1
             