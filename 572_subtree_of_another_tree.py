# Definition for a binary tree node.
from typing import Optional
'''
This approach checks whether `subRoot` is a subtree of `root` using iterative tree traversal and comparison.

We use a Depth-First Search (DFS) approach by maintaining a `root_stack` to traverse every node in the `root` tree.

For each node in the `root` tree:
- If the node’s value matches the root of `subRoot`, we begin a subtree comparison.
- We use a `valid_stack` to iteratively compare the subtree starting at this node with `subRoot`.
- Nodes are compared pairwise:
  - If both nodes are `None`, we continue.
  - If only one is `None` or their values differ, we mark the subtree as invalid.
  - If they match, we push their left and right children onto the stack to compare recursively.

If a matching subtree is found, we return `True`.
If no match is found after checking all nodes, we return `False`.

--> Time Complexity

Let `n` be the number of nodes in `root`, and `m` be the number of nodes in `subRoot`.

- In the worst case, we may check each of the `n` nodes in `root` as a potential match.
- For each potential match, we compare up to `m` nodes in `subRoot`.

Total Time Complexity: O(n * m)

--> Space Complexity

- The `root_stack` can store up to O(n) nodes in the worst case.
- The `valid_stack` used during subtree comparison can store up to O(m) pairs.

Total Space Complexity: O(n + m)
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_stack = [root]
        while root_stack:
            root_node = root_stack.pop()
            if root_node.val == subRoot.val:
                is_valid = True
                valid_stack = [(root_node, subRoot)]
                while valid_stack:
                    l_node, r_node = valid_stack.pop()
                    if not l_node and not r_node:
                        continue
                    if not l_node or not r_node:
                        is_valid = False
                        break
                    if l_node.val != r_node.val:
                        is_valid = False
                        break
                    valid_stack.append((l_node.left, r_node.left))
                    valid_stack.append((l_node.right, r_node.right))

                if is_valid:
                    return True

            if root_node.left: 
                root_stack.append(root_node.left)
            if root_node.right: 
                root_stack.append(root_node.right)
        
        return False

            
