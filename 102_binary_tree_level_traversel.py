from collections import deque
from typing import List, Optional
# Definition for a binary tree node.
'''
This approach performs a level order traversal (Breadth-First Search) on a binary tree.

Core Idea:
- Traverse the tree level by level using a queue (deque).
- For each level, store the values of the nodes in a list.
- Append each level's list to the final output list.

Level Order Logic:
- Use a deque to process nodes in FIFO manner.
- At each level, we process all nodes currently in the queue (which belong to that level).
- Add the left and right children of each node to the queue for the next level.

--> Time Complexity

Level Order Traversal:
- Every node is visited exactly once.
- Let n be the total number of nodes in the binary tree.

Total Time Complexity: **O(n)**

--> Space Complexity

- Uses a queue to keep track of nodes at each level.
- In the worst case (for a complete binary tree), the queue can hold up to n/2 nodes.

Total Space Complexity: **O(n)**
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs
        if not root:
            return []
        stack= deque([root])
        output = []
        while stack:
            level_list = []
            level_size = len(stack)
            for _ in range(level_size):
                node = stack.popleft()
                level_list.append(node.val)
                if node.left: 
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            output.append(level_list)
        return output


