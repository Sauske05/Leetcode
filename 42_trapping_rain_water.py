from typing import List
'''
In this approach, we use two auxiliary arrays: max_left and max_right.
Each stores the maximum height to the left and right of every index, respectively.

--> Time Complexity
The algorithm runs in O(n) time:
- One pass to fill max_left
- One pass to fill max_right
- One pass to calculate trapped water

--> Space Complexity
O(n) space is required to store the max_left and max_right arrays.


While the solution is correct and intuitive, it's suboptimal in terms of space.
It uses O(n) extra space, which can be avoided. The two-pointer technique is preferred.
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        max_l_num = height[0]
        max_r_num = height[-1]
        for i in range(len(height)):
            max_left[i] = max(height[i], max_l_num)
            max_l_num = max(height[i], max_l_num)
        
        for i in range(len(height)-1, -1, -1):
            max_right[i] = max(height[i], max_r_num)
            max_r_num = max(height[i], max_r_num)
        
    
        return sum([0 if (min(max_right[i], max_left[i]) - height[i]) < 0 else (min(max_right[i], max_left[i]) - height[i]) for i in range(len(height))])


'''
This is the optimal two-pointer approach.

--> Time Complexity
The algorithm runs in O(n) time:
- Single pass with two pointers traversing from both ends

--> Space Complexity
O(1) additional space is used since we don’t store extra arrays


This solution is optimal because it avoids extra memory usage.
It dynamically tracks left_max and right_max and accumulates trapped water 
based on the lower side, ensuring correctness in one pass.
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        trap_amount = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                trap_amount += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                trap_amount += max(0, right_max - height[right])
        
        return trap_amount

