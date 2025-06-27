# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
This approach adds two numbers represented by linked lists in reverse order, digit by digit.

--> Time Complexity
O(max(n, m)), where n and m are the lengths of l1 and l2:
- Each node is visited once
- Addition and carry propagation are constant-time operations

--> Space Complexity
O(max(n, m)) for the result list:
- One new node is created per digit in the sum
- A dummy node simplifies head tracking

Key Details:
- A dummy node is initialized to simplify the result list construction
- A `carry` is maintained throughout the traversal
- At each step, values from l1 and l2 are added along with carry, and the result is appended as a new node
- The loop continues as long as there are nodes in l1, l2, or a non-zero carry

The solution is efficient and clean, ensuring proper handling of uneven-length inputs and final carry.
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(float('inf'))
        current_node = dummy_node
        carry = 0
        while l1 or l2 or (carry > 0):
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            current_val = l1_val + l2_val + carry
            carry = current_val // 10  
            current_val = current_val % 10
            new_node = ListNode(current_val)
            current_node.next = new_node
            current_node = current_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        return dummy_node.next

        
        