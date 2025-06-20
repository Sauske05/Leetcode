from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
This approach uses Floyd’s Tortoise and Hare algorithm (two-pointer technique) 
to detect if a cycle exists in a singly linked list.

1. Two pointers, `slow` and `fast`, are initialized at the head.
2. In each iteration of the loop:
   - `slow` moves one step forward.
   - `fast` moves two steps forward.
3. If there is no cycle, `fast` will eventually reach the end (None), and we return False.
4. If there is a cycle, `fast` will eventually meet `slow` within the cycle, and we return True.

Why this works: In a cyclic list, `fast` moves through the cycle quicker than `slow`,
and thus will eventually "lap" and meet `slow`.

--> Time Complexity

In the worst case (no cycle), `fast` travels the entire length of the list.

If there is a cycle, the pointers will meet in at most O(n) steps, 
where n is the number of nodes before the cycle starts plus the cycle length.

Total Time Complexity: O(n)

--> Space Complexity

Only two pointers (`slow` and `fast`) are used regardless of list size.

Total Space Complexity: O(1)
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

            