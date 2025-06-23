# Definition for a binary tree node.
from typing import Optional
'''
This approach uses **iterative Depth-First Search (DFS)** with a stack to calculate the **maximum depth** of a binary tree.

The **maximum depth** (or height) of a binary tree is defined as the number of nodes along the longest path from the root down to the farthest leaf node.

--> How It Works:

1. If the root is `None`, return 0 — the tree is empty.
2. Initialize a stack with the root node and its current level (1).
3. Traverse the tree iteratively:
   - Pop a node and its level from the stack.
   - Push its left and right children (if any) onto the stack, each with `level + 1`.
   - Keep updating the `max_level` to track the deepest level encountered.

--> Time Complexity

Each node is visited exactly once.

- Let n be the number of nodes in the tree.

Total Time Complexity: **O(n)**

--> Space Complexity

- The stack holds at most O(h) elements at any time, where h is the height of the tree.

    - Worst-case (skewed tree): O(n)
    - Best-case (balanced tree): O(log n)

Total Space Complexity: **O(h)**

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 1
        max_level = level
        stack = [(root, level)]
        while stack:
            node, level = stack.pop()
            if node.left: 
                stack.append((node.left, level +1))
            if node.right: 
                stack.append((node.right, level +1))
            max_level = max(level, max_level)
        return max_level

