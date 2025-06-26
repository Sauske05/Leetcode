# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
In this approach, we count the number of "good nodes" in a binary tree using an iterative
DFS (Depth-First Search) traversal with a stack. A node is considered "good" if its value
is greater than or equal to the maximum value along the path from the root to that node.

The logic:
1. Start traversal from the root, initializing a stack with a tuple of (node, max_value_so_far).
2. At each step:
   - If the current node's value is greater than or equal to the max seen so far, increment the count.
   - Push the left and right children to the stack, updating the max value along the path.
3. Continue until all nodes have been visited.

--> Time Complexity

Each node is visited exactly once: O(n), where n is the number of nodes in the tree.
All operations within the loop (comparisons and stack operations) are constant time.

Total Time Complexity: O(n)

--> Space Complexity

In the worst case, the stack can grow up to the height of the tree: O(h),
where h is the height of the binary tree.

Total Space Complexity: O(h)
'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        stack = [(root, root.val)]
        #max_node:int = root.val
        while stack:
            node, max_val = stack.pop()
        
            if node.val >= max_val:
                self.count +=1
            if node.left: 
                stack.append((node.left, max(node.left.val, max_val)))

            if node.right: 
                stack.append((node.right, max(node.right.val, max_val)))
        return self.count
