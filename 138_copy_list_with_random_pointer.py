# Definition for a Node.
from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
'''
This approach performs a deep copy of a **complex linked list** where each node contains:
- A `next` pointer to the next node in the list.
- A `random` pointer that may point to any node in the list (or be null).

Problem Insight:
- We must create a new linked list such that each node is a copy of the original node.
- The copied list should preserve both `next` and `random` pointer relationships.

Strategy Using HashMap:
1. **First Pass:**
   - Traverse the original list.
   - For each node, create a copy and store it in a hash map where the key is the original node and the value is the copied node.

2. **Second Pass:**
   - Traverse the original list again.
   - Use the hash map to assign `next` and `random` pointers to the copied nodes.
   - For example, `copy_node.next = hash_map[original_node.next]`

3. **Return the new head**, which is the copy of the original head node.

Benefits:
- This approach ensures that the `random` pointer (which could point to a node that hasn’t been created yet) is safely resolved in the second pass.

--> Time Complexity:
- O(n): Each of the two passes takes O(n) time where n is the number of nodes.

--> Space Complexity:
- O(n): A hash map of size `n` is used to store the mapping between original and copied nodes.

'''
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        while not head:
            return None
        hash_map = {}
        curr = head
        #Mapping the nodes withh the values 
        while curr:
            hash_map[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            hash_map[curr].next = hash_map.get(curr.next, None)
            hash_map[curr].random = hash_map.get(curr.random, None)
            curr = curr.next

        return hash_map[head]

