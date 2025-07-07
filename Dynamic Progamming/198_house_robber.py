from typing import List
'''
This implementation solves the "House Robber" problem using bottom-up Dynamic Programming.

Problem Summary:
- You are given a list of non-negative integers representing the amount of money in each house.
- You cannot rob two adjacent houses.
- The goal is to determine the maximum amount of money that can be robbed without triggering the alarm.

--> Time Complexity
- O(n), where n is the length of the input list `nums`
- We iterate through the list once, updating the DP table in constant time

--> Space Complexity
- O(n), due to the use of an auxiliary list `output` of size equal to `nums`
- This can be optimized to O(1) space using two variables instead of a full list

Key Details:
- `output[i]` stores the maximum amount of money that can be robbed from the first `i+1` houses
- For each house at index `i`, we decide whether to:
    - Rob it and add its value to `output[i-2]`, OR
    - Skip it and carry forward `output[i-1]`
- The recurrence relation is:
    - output[i] = max(output[i-1], output[i-2] + nums[i])
- The final answer is stored at `output[-1]`, which contains the result for all houses

This DP approach ensures optimal decisions at every step and avoids redundant calculations typical of recursive solutions.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
    
        if len(nums) < 2:
            return nums[-1]

        output = [0] * len(nums)
        output[0] = nums[0]
        output[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            output[i] = max(output[i-1], output[i-2] + nums[i])

        return output[-1]
