# Definition for a binary tree node.
from typing import Optional
'''
This approach solves the **Maximum Path Sum** in a binary tree where the path can start and end at any node.

--> Strategy

1. Use a Depth-First Search (DFS) traversal to explore each node.
2. For each node, calculate:
   - The maximum path sum from the left subtree (ignoring negative paths by using `max(left, 0)`).
   - The maximum path sum from the right subtree (also ignoring negative paths).
3. The local path sum at that node is `left + right + node.val`, which considers both children and the node itself.
   - Update the global maximum (`self.max_val`) with this local sum if it's higher.
4. Return `node.val + max(left, right)` to the parent call, as only one side (left or right) can be included in the continuing path upward.

--> Why ignore negative paths?

Including negative paths would reduce the total path sum, so we treat them as 0.

--> Time Complexity

- O(n): Every node is visited once.

--> Space Complexity

- O(h): Due to recursion stack, where `h` is the height of the tree (O(log n) for balanced, O(n) for skewed).

This recursive DFS efficiently computes the highest sum path that may branch out at any node.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_val = float('-inf')
        def dfs(current):
            if not current:
                return 0
            left:int = max(dfs(current.left), 0)
            right:int = max(dfs(current.right), 0)
            
            self.max_val = max(self.max_val, left+right+current.val)
            return current.val + max(left, right)
        
        dfs(root)
        return self.max_val