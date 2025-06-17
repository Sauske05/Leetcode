from typing import List, Tuple
'''
This approach solves the problem using a *monotonic decreasing stack* pattern.
We traverse the temperature list in reverse order and maintain a stack that keeps track of indices of temperatures in decreasing order.
The stack helps us efficiently find the next warmer day for each day.

--> Time Complexity

Loop: We iterate through the temperature list once, from the end to the beginning — O(n), where n is the number of days.

Stack Operations:
- Each element is pushed and popped at most once.
- In the worst case (strictly decreasing temperatures), each temperature is pushed and then popped — O(n) total stack operations.

Total Time Complexity: O(n)

--> Space Complexity

Stack: The stack stores at most n elements in the worst case — O(n) space.

Output List: The result list has size n — O(n) space.

Total Space Complexity: O(n) + O(n) = O(n)

--> Intuition

- By traversing from right to left, we ensure that the top of the stack always holds the nearest future day with a higher temperature.
- If current temperature is less than the one on top of the stack, we compute the difference in days.
- Otherwise, we pop from the stack until we find a warmer future day or the stack becomes empty.
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: List[Tuple] = []
        output = [0] * len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            
            if stack:
                output[i] = stack[-1][1] - i
            
            stack.append((temperatures[i], i))
        
        return output