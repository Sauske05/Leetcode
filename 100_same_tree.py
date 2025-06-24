# Definition for a binary tree node.
from typing import Optional
'''
This approach checks whether two binary trees `p` and `q` are structurally identical and have the same node values.

We use an iterative method with a stack to simulate a synchronized traversal of both trees.

Steps:
- Initialize a stack with the root nodes of both trees.
- While the stack is not empty:
    - Pop a pair of nodes `(p_el, q_el)` from the stack.
    - If both nodes are `None`, continue to the next pair (this means both subtrees are empty).
    - If only one of them is `None`, the trees differ in structure — return `False`.
    - If their values differ, the trees differ in content — return `False`.
    - Otherwise, push the left children and right children of both nodes into the stack for further comparison.

If the entire traversal completes without mismatches, return `True`, indicating the trees are the same.

--> Time Complexity

Each node in both trees is visited once.

Let `n` be the number of nodes in tree `p` and `m` in tree `q`.

Total Time Complexity: O(min(n, m)) — worst case O(n) if both trees are the same size.

--> Space Complexity

- The stack may grow up to the height of the tree in the worst case.

Total Space Complexity: O(h), where `h` is the maximum height of the trees.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            p_el , q_el = stack.pop()
            if not p_el and not q_el: #both are None
                continue
            if not p_el or not q_el: #if any is None
                return False
            if p_el.val != q_el.val:
                return False
            stack.append((p_el.left, q_el.left))
            stack.append((p_el.right, q_el.right))

        return True