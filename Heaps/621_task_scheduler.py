from collections import Counter, deque, List
import heapq
"""
This is an efficient solution to the 'Task Scheduler' problem using a max-heap and a cooldown queue.

--> Problem Summary:
Given a list of CPU tasks (identified by capital letters) and a cooldown interval `n`, determine the least number of units of time required to finish all tasks such that the same task is executed at least `n` units apart.

--> Time Complexity:
- O(n log k), where n is the number of tasks and k is the number of unique tasks.
    - Each heap push/pop is log k, and each task is pushed/popped once.
- Space Complexity: O(k)
    - For the heap and the cooldown queue (`stack`), which both store at most k items.

--> Approach:
- Count the frequency of each task using `Counter`.
- Use a max-heap (simulated with negative values) to always schedule the task with the highest remaining frequency.
- At each unit of time:
    - If the heap is not empty, schedule the most frequent task.
        - Decrement its count and push it into a cooldown `stack` (with the time when it can be scheduled again).
    - Check if any task in `stack` has completed its cooldown (i.e., its release time equals current time).
        - If yes, push it back to the heap.
- Repeat until both heap and stack are empty.
- The final value of `count` gives the total time required to finish all tasks with valid cooldowns.

This greedy + heap approach ensures optimal CPU utilization while respecting the cooldown requirement.
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_map = Counter(tasks)
        stack = deque([])
        heap = [-v for _, v in count_map.items()]
        heapq.heapify(heap)
        count = 0
        while heap or stack:
            count +=1
            if heap:
                task = 1 + heapq.heappop(heap)
                
                if task: #task is not 0
                    stack.append((task, count+n))
            if stack and stack[0][1] == count:
                heapq.heappush(heap,stack.popleft()[0])
        return count

