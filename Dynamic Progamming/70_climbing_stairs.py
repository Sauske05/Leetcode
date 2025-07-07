'''
This implementation solves the classic "Climbing Stairs" problem using bottom-up Dynamic Programming.

Problem Summary:
- You are climbing a staircase with `n` steps.
- You can climb either 1 or 2 steps at a time.
- The goal is to determine in how many distinct ways you can reach the top.

--> Time Complexity
- O(n), where n is the total number of stairs
- We compute the result iteratively from step 2 to n

--> Space Complexity
- O(n), due to the use of a list `stack` of size (n+1)
- Can be optimized to O(1) using two variables for previous steps

Key Details:
- `stack[i]` stores the number of distinct ways to reach step `i`
- Base cases:
    - There is 1 way to reach step 0 (do nothing)
    - There is 1 way to reach step 1 (one single step)
- The recurrence relation:
    - stack[i] = stack[i-1] + stack[i-2]
    - From step `i`, you can come either from step `i-1` or `i-2`
- Final answer is stored in `stack[n]`

This problem is essentially the Fibonacci sequence shifted by one index and is a fundamental example of DP in combinatorics.
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        stack = [1] * (n+1)

        for i in range(2, len(stack)):
            stack[i] = stack[i-1] + stack[i-2]

        return stack[-1]

