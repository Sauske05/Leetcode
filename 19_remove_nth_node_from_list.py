from typing import Optional
# Definition for singly-linked list.
'''
This approach removes the **n-th node from the end** of a singly linked list in **one pass** using the two-pointer technique.

Problem Insight:
- We're given a linked list and an integer `n`, and we need to delete the n-th node **from the end** of the list.
- A naïve approach would involve two passes:
  1. Count total nodes.
  2. Delete the (length - n)-th node.
- However, we can do this in **one traversal** using a fast and slow pointer.

Two-Pointer Strategy with Dummy Node:
1. **Initialize a dummy node** pointing to head to simplify edge cases (e.g., removing the head itself).
2. **Set both fast and slow pointers** to the dummy node.
3. **Move the fast pointer n steps ahead** — this creates a gap of `n` between fast and slow.
4. **Move both fast and slow pointers forward** until fast reaches the end.
   - At this point, `slow` is just before the node to be removed.
5. **Skip the target node** by adjusting `slow.next`.

Why use a dummy node?
- It helps handle corner cases uniformly, like when the head node is the one to be removed.

--> Time Complexity:
- O(n): Single pass over the list.

--> Space Complexity:
- O(1): Constant space usage (just pointers).

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(float('-inf'))
        dummy_node.next = head
        slow, fast = dummy_node, dummy_node
        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        if slow:
            slow.next = slow.next.next
        
        return dummy_node.next
