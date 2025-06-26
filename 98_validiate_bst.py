from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
In this approach, we validate whether a binary tree is a Binary Search Tree (BST) using a 
recursive Depth-First Search (DFS). A tree is a valid BST if for every node:
- All nodes in its left subtree are strictly less than the node’s value.
- All nodes in its right subtree are strictly greater than the node’s value.

The logic:
1. Start DFS with an initial valid range from negative to positive infinity.
2. At each node:
   - If the node’s value is not within the valid (lower, upper) bounds, mark the tree as invalid.
   - Recursively validate the left subtree with an updated upper bound (current node’s value).
   - Recursively validate the right subtree with an updated lower bound.
3. Early stop if any violation is detected.

--> Time Complexity

Each node is visited exactly once: O(n), where n is the number of nodes in the tree.

Total Time Complexity: O(n)

--> Space Complexity

The recursion stack depends on the height of the tree:
- Worst case (unbalanced tree): O(n)
- Best case (balanced tree): O(log n)

Total Space Complexity: O(h), where h is the height of the tree.
'''

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_valid = True

        def dfs(node, lower, upper):
            if not node or not self.is_valid:
                return
            if not (lower < node.val < upper):
                self.is_valid = False
                return
            dfs(node.left, lower, node.val)
            dfs(node.right, node.val, upper)

        dfs(root, float('-inf'), float('inf'))
        return self.is_valid

            