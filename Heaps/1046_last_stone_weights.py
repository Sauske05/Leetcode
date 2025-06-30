import heapq
from typing import List
"""
This is the optimal solution to the 'Last Stone Weight' problem using a Max-Heap.

--> Time Complexity
The algorithm runs in O(n log n) time:
- Building the heap takes O(n).
- Each extraction and insertion operation on the heap takes O(log n), and we perform this up to n times.

--> Space Complexity
O(n) space:
- A heap of size at most n is maintained during the process.

This approach uses a max-heap to always fetch the two heaviest stones efficiently. 
Since Python’s `heapq` implements a min-heap by default, we negate the weights to simulate max-heap behavior. 
At each step, the two heaviest stones are smashed together. If their weights are unequal, the remaining difference 
is pushed back into the heap. This continues until one or zero stones are left.
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = [-x for x in stones]
        heapq.heapify(self.stones)

        while len(self.stones) > 1: #At least two stones
            x = -heapq.heappop(self.stones)
            y = -heapq.heappop(self.stones)  
            if x != y:
                heapq.heappush(self.stones, -x+y)
        print(self.stones)
        if not self.stones:
            return 0
        else: 
            return -self.stones[0]

            

