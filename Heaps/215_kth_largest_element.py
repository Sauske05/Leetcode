import heapq
from typing import List
"""
This is an efficient solution to the 'Kth Largest Element in an Array' problem using a Min-Heap.

--> Problem Summary:
Given an integer array `nums` and an integer `k`, return the kth largest element in the array.

--> Time Complexity:
- O(n log k), where n is the number of elements in the array.
    - We maintain a heap of size k and perform log k operations during heap insertion/removal.

--> Space Complexity:
- O(k): We maintain a heap with at most k elements at any time.

--> Approach:
- Convert the array into a Min-Heap in-place using `heapq.heapify(nums)`.
- Continuously pop the smallest element until only `k` elements remain.
    - After popping n - k elements, the smallest in the heap is the kth largest overall.
- Return `nums[0]`, which is the root of the Min-Heap and represents the kth largest element.

This is a clean and memory-efficient approach for finding the kth largest value without fully sorting the array.
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]