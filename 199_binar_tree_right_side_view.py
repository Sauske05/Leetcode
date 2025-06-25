from collections import deque
from typing import Optional, List
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
This approach finds the right-side view of a binary tree using level order traversal (BFS).

Core Idea:
- We traverse the tree level by level (using a queue).
- For each level, we prioritize visiting the **right child before the left child**.
- The first node encountered at each level (from right to left) is the visible node from the right side.

Level Order Logic:
- Use a deque to perform BFS.
- For each level, store the node values in a list (`level_res`).
- Append right child first to ensure that the rightmost node is visited first at the next level.

--> Time Complexity

Level Order Traversal:
- Each node is visited exactly once.
- Total nodes = n, where n is the number of nodes in the tree.

Total Time Complexity: **O(n)**

--> Space Complexity

- Uses a queue (`stack`) for level order traversal.
- Worst-case space usage is proportional to the maximum number of nodes at any level (up to n/2 in a balanced tree).

Total Space Complexity: **O(n)**
'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        results = []
        stack = deque([root])
        while stack:
            level_res = []
            for _ in range(len(stack)):
                node = stack.popleft()
                level_res.append(node.val)

                if node.right: 
                    stack.append(node.right)
                if node.left: 
                    stack.append(node.left)
            results.append(level_res)
        
        return [i[0] for i in results]


        
                
