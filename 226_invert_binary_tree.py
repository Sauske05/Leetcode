from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
This approach uses **iterative Depth-First Search (DFS)** via a stack to invert a binary tree.

Inversion means swapping the left and right children of all nodes in the tree.

--> How It Works:

1. If the root is None, return None.
2. Use a stack initialized with the root node.
3. While the stack is not empty:
    - Pop a node from the stack.
    - If it has a left child, push it to the stack.
    - If it has a right child, push it to the stack.
    - Swap its left and right children.

The tree is modified in-place during traversal.

--> Time Complexity

Each node is visited exactly once.

- Let n be the number of nodes in the tree.

Total Time Complexity: **O(n)**

--> Space Complexity

- The stack can grow up to O(h), where h is the height of the tree.

    - Worst-case (unbalanced tree): O(n)
    - Best-case (balanced tree): O(log n)

Total Space Complexity: **O(h)**
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #dfs traversal
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            temp = node.left
            node.left = node.right
            node.right = temp
        return root