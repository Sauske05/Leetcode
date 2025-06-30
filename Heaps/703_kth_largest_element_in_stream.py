import heapq
from typing import List
"""
This is an efficient solution to the 'Kth Largest Element in a Stream' problem using a Min-Heap.

--> Time Complexity
- Constructor: O(n log k), where n is the number of initial elements. We maintain only k elements in the heap.
- add(): O(log k) for each insertion/removal operation.

--> Space Complexity
O(k) space:
- The heap stores only the k largest elements seen so far.

This approach maintains a min-heap of size k.
- The smallest element in the heap is always the kth largest among all inserted elements.
- When a new number is added:
   - It's pushed into the heap.
   - If the heap exceeds size k, the smallest element is popped out.
- This ensures the top of the heap (`heap[0]`) is always the kth largest element.

This method is optimal for handling real-time data streams where you need quick updates and lookups.
"""
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        #print(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)