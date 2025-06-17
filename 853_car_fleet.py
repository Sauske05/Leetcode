from typing import List, Tuple
'''
This approach solves the "Car Fleet" problem using a monotonic *decreasing stack* based on time-to-target.
We simulate how cars approach the target, forming fleets only if a slower car cannot catch the car ahead.

Key Insight:
- A car can never pass another car, but it can catch up and form a fleet.
- We sort cars by position in descending order and compute the time each car will take to reach the target.
- If the current car takes more time than the car ahead (on the stack), it cannot catch up, hence forms a new fleet.

--> Time Complexity

Sorting: We sort the position-speed pairs by position in descending order — O(n log n), where n is the number of cars.

Loop: We iterate over the sorted list once — O(n).

Each element is pushed to the stack at most once, and the check is constant time — O(n).

Total Time Complexity: O(n log n) due to sorting.

--> Space Complexity

Pair List: The position_speed list holds n elements — O(n) space.

Stack: At most n elements are pushed to the stack — O(n) space.

Total Space Complexity: O(n) + O(n) = O(n)

--> Intuition

- By sorting from the car nearest to the target, we simulate how cars reach the destination.
- If a car behind catches up to a slower car, it forms a fleet and adopts its slower pace.
- We use a stack to track fleet arrival times — if the current car takes longer, it can't merge with the fleet ahead.
'''
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack:List[int] = []
        position_speed: List[Tuple] = [(position[i], speed[i]) for i in range(len(position))]
        position_speed.sort(key = lambda x: x[0], reverse = True)
        
        for i in range(len(position_speed)):
            time_taken = (target - position_speed[i][0])/ position_speed[i][1]
            if not stack:
                stack.append(time_taken)

            if time_taken > stack[-1]:
                stack.append(time_taken)
            

        return len(stack)