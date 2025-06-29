from collections import deque
# Definition for a binary tree node.
'''
This approach serializes and deserializes a binary tree using level-order traversal (BFS).

--> Serialization

1. Traverse the tree using a queue (BFS).
2. For each node, store its value in the list.
   - If the node is None (i.e. missing child), append a placeholder symbol '%' to preserve structure.
3. Convert the list into a comma-separated string.

--> Deserialization

1. Convert the serialized string back into a list of node values.
2. Reconstruct the tree using a queue (BFS).
   - Start with the root node created from the first value.
   - For each node in the queue:
     - Assign the next value as the left child (if not '%') and enqueue it.
     - Assign the following value as the right child (if not '%') and enqueue it.
3. Continue until the entire list is processed.

This process guarantees that the original structure of the binary tree is maintained during both serialization and deserialization.

--> Time Complexity

- Serialization: O(n) — Each node is visited once during BFS.
- Deserialization: O(n) — Each node is reconstructed exactly once.

--> Space Complexity

- O(n) for storing the serialized string list.
- O(n) for the queue used in both serialization and deserialization.

This method is robust for trees with null/missing children, as it explicitly encodes their positions using placeholders.
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
    
        queue = deque([root])
        ser_list = []

        while queue:
            node = queue.popleft()
            if node:
                ser_list.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                ser_list.append('%') 

        return ','.join(ser_list)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        res_list = data.split(',')
        root = TreeNode(int(res_list[0]))
        stack = deque([root])
        i = 1
        while stack and i < len(res_list):
            node = stack.popleft()
            #insert into left
            if res_list[i] != '%':
                node.left = TreeNode(int(res_list[i]))
                stack.append(node.left)
            i +=1
            #Right
            if i < len(res_list) and res_list[i] != '%':
                node.right = TreeNode(int(res_list[i]))
                stack.append(node.right)
            i +=1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))