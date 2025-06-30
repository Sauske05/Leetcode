import heapq
from typing import List

"""
This is an efficient solution to the 'K Closest Points to Origin' problem using a Min-Heap.

--> Time Complexity
- O(n + k log n):
    - Building the heap takes O(n).
    - Extracting the k closest points takes O(k log n).

--> Space Complexity
- O(n) space:
    - We store distances and their corresponding indices in a heap.

Approach:
- We calculate the squared Euclidean distance (x² + y²) for each point to avoid unnecessary square root operations.
- Store each point’s distance along with its original index.
- Convert this list to a min-heap based on distance.
- Pop the heap k times to get the k closest points to the origin.

By storing indices instead of coordinates directly, we avoid duplicating point data and can access the original list cleanly.
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [(x**2 + y**2, i) for i, (x, y) in enumerate(points)]
        heapq.heapify(distance)
        output = []
        count = 0
        while count < k:
            _,  i = heapq.heappop(distance)
            output.append(points[i])
            count +=1

        return output
        
