# Definition for a binary tree node.

'''
This approach finds the Lowest Common Ancestor (LCA) of two nodes in a binary tree using parent mapping.

Core Idea:
- Traverse the tree using DFS (with an explicit stack) and record each node's parent in a dictionary.
- Once we have parent information for all nodes, we trace the path from `p` to the root and store all ancestors in a set.
- Then, we trace the path from `q` upward until we find a node that appears in `p`'s ancestor set — this node is the LCA.

Parent Mapping Logic:
- Start with the root node and initialize its parent as `None`.
- While traversing, assign each child node's parent to the current node.
- This builds a complete parent reference for each node in the tree.

--> Time Complexity

Traversal + Ancestor Lookup:
- We traverse all nodes once to build the parent map ⇒ O(n)
- Then trace paths from `p` and `q` to root ⇒ O(h + h), where h = height of tree

Total Time Complexity: **O(n)**

--> Space Complexity

- Dictionary for storing parent references of all nodes ⇒ O(n)
- Set to store ancestors of `p` ⇒ O(h), where h = height of tree

Total Space Complexity: **O(n)**
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_dict = {root: None}
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                parent_dict[node.left] = node
            if node.right:
                stack.append(node.right)
                parent_dict[node.right] = node
        
        
        #print(parent_dict[p])
        #print(parent_dict[q])

        parents_set = set()
        while p:
            parents_set.add(p)
            p = parent_dict[p]
        
        while q not in parents_set:
            q = parent_dict[q]

        return q
        