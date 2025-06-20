from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
In this approach, we reverse the singly linked list iteratively using three pointers: 
`current` to track the node being processed, `prev` to store the previous node (which will be the new `next`), 
and `tmp` to temporarily store the next node before breaking the current link.

The logic:
1. Traverse through the list.
2. At each step, store `current.next` in a temporary variable.
3. Point `current.next` to `prev` (reverse the link).
4. Move `prev` to `current` and `current` to `tmp`.
5. At the end, `prev` will be the new head of the reversed list.

--> Time Complexity

Traversing through the entire linked list of `n` nodes takes O(n).
All operations inside the loop (pointer assignments) are O(1).

Total Time Complexity: O(n)

--> Space Complexity

We use only a few pointers (`prev`, `current`, and `tmp`), which take constant space.

Total Space Complexity: O(1)
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current:
            tmp = current.next
            #prev = current
            current.next = prev
            prev = current
            current = tmp
        
        return prev

