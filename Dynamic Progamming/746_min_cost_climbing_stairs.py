from typing import List
'''
This implementation solves the "Min Cost Climbing Stairs" problem using bottom-up Dynamic Programming.

Problem Summary:
- You are given an array `cost` where `cost[i]` is the cost of stepping on the ith stair.
- You can start at step 0 or step 1.
- At each move, you can climb either one or two steps.
- The goal is to reach the top (one step beyond the last index) with the minimum cost.

--> Time Complexity
- O(n), where n is the length of the `cost` list
- Each index is visited exactly once during iteration

--> Space Complexity
- O(n), due to the use of the auxiliary list `output` to store minimum costs for each step
- This can be optimized to O(1) by using two variables instead of a list

Key Details:
- The `cost` list is extended by appending a `0` to represent the top of the staircase (no cost to step off).
- `output[i]` stores the minimum cost to reach step `i`
- At each step, we decide whether to come from the previous step or the one before that:
    - output[i] = min(output[i-1], output[i-2]) + cost[i]
- The final value `output[-1]` gives the minimum cost to reach the top

This approach ensures that at every step, the globally optimal choice is made based on previously computed results.
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        output = [1] * len(cost)

        output[0], output[1] = cost[0], cost[1]
        for i in range(2, len(output)):
            output[i] = min(output[i-1], output[i-2]) + cost[i]

        return output[-1]