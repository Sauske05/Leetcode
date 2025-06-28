import heapq
# Definition for singly-linked list.
from typing import List, Optional
'''
This approach uses a **Min-Heap (Priority Queue)** to efficiently merge K sorted linked lists into one.

1. Initialize a min-heap to keep track of the smallest current node from each list.
2. Insert the first node of each non-empty list into the heap. 
   - Each entry in the heap is a tuple (node value, list index, node), ensuring a unique and sortable structure.
3. Create a dummy node to simplify result list construction and a pointer `curr` to track the end of the merged list.
4. While the heap is not empty:
   - Pop the smallest node from the heap.
   - Append it to the merged list (`curr.next = node`).
   - Move the `curr` pointer forward.
   - If the popped node has a `next` node, push that `next` node into the heap.

Why this works: The heap maintains the invariant that the smallest available node is always at the top,
which allows merging to proceed in sorted order without scanning all K lists each time.

--> Time Complexity

- Building the initial heap takes O(K log K), where K is the number of lists.
- Each of the N total nodes is pushed and popped from the heap once, each heap operation costing O(log K).

Total Time Complexity: O(N log K), where N is the total number of nodes across all lists.

--> Space Complexity

- The heap contains at most K elements at any time.

Total Space Complexity: O(K)
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy_node = ListNode(float('inf'))
        curr = dummy_node

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy_node.next