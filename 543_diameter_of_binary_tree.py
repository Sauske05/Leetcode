# Definition for a binary tree node.
from typing import Optional
'''
This approach uses Depth-First Search (DFS) to calculate the height of each subtree
while simultaneously tracking the maximum diameter encountered.

The **diameter** of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

For each node:
- We recursively calculate the height of the left and right subtree.
- The path through this node is `left + right`, and we update the global maximum accordingly.
- The function returns `max(left, right) + 1` to inform the parent of its height.

--> Time Complexity

Each node is visited exactly once in the DFS traversal.

- For n nodes, the traversal takes O(n) time.

Total Time Complexity: **O(n)**

--> Space Complexity

- The recursion stack will go as deep as the height of the tree. In the worst case (completely unbalanced), the height could be O(n). 
  In the best case (balanced tree), it will be O(log n).

- No additional data structures are used.

Total Space Complexity: **O(h)**, where h is the height of the tree. Worst case: O(n), Best case: O(log n)
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def dfs(current:Optional[TreeNode]) -> int:
            if not current:
                return 0
            left = dfs(current.left)
            right = dfs(current.right)
            self.max_diameter = max(self.max_diameter, left + right)
            return max(left, right) + 1
        dfs(root)
        return self.max_diameter