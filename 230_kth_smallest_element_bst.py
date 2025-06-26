from typing import Optional
import heapq
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        '''
In this approach, we use a max heap of size `k` to keep track of the k smallest elements
encountered during the traversal of the binary tree. Since Python only provides a min-heap
via `heapq`, we push the negative of each value to simulate a max-heap.

The logic:
1. Perform a DFS traversal using a stack (iterative approach).
2. For each visited node:
   - Push the negative of its value into the heap.
   - If the heap size exceeds `k`, pop the largest value (which is the smallest in terms of original value).
3. At the end of the traversal, the root of the heap will contain the k-th smallest value (as a negative number),
   so we return its negation.

--> Time Complexity

Each node is visited once: O(n) where n is the number of nodes in the tree.
Each heap operation (push and pop) takes O(log k), and we maintain the heap size at most k.

Total Time Complexity: O(n log k)

--> Space Complexity

- Heap stores at most `k` elements: O(k)
- Stack may grow up to the height of the tree in worst case: O(h), where h is the height of the tree.

Total Space Complexity: O(k + h)
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        stack = [root]
        while stack:
            node = stack.pop()
            heapq.heappush(heap, -node.val)
            if len(heap) > k:
                heapq.heappop(heap)
                
            if node.left: 
                stack.append(node.left)
            if node.right: 
                stack.append(node.right)
        #print(heap)
        return -heap[0]

        