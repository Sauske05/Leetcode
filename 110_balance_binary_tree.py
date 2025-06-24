# Definition for a binary tree node.
from typing import Optional
'''
This approach checks whether a binary tree is height-balanced using Depth-First Search (DFS).

A binary tree is considered height-balanced if, at every node, the difference in height between the left and right subtrees is at most 1.

Steps:
- If the tree is empty (`root is None`), it is trivially balanced.
- We define a helper function `dfs(current)` that:
    - Recursively computes the height of the left and right subtrees.
    - Checks if the absolute difference in heights is greater than 1. If so, it marks the tree as unbalanced by setting `self.is_valid = False`.
    - Returns the height of the current subtree, which is `1 + max(left_height, right_height)`.
- The `self.is_valid` flag is used to track the balance status globally during traversal.
- After the full traversal, we return the value of `self.is_valid`.

--> Time Complexity

Each node is visited exactly once during DFS traversal.

Let `n` be the number of nodes in the tree.

Total Time Complexity: O(n)

--> Space Complexity

- The maximum space used is proportional to the height of the recursion stack.

Best case (balanced tree): O(log n)  
Worst case (skewed tree): O(n)

Total Space Complexity: O(h), where `h` is the height of the tree.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.is_valid = True
        def dfs(current):
            if not current:
                return 0
            left = dfs(current.left)
            right = dfs(current.right)
            if abs(left- right) > 1:
                self.is_valid = False
            return 1 + max(left, right)
        dfs(root)
        return self.is_valid