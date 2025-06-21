from typing import Optional
'''
This approach reorders a singly linked list in a specific pattern:

Given a linked list `L0 → L1 → L2 → ... → Ln-1 → Ln`,  
Reorder it to: `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...`

Constraints:
- You must do this **in-place** without modifying the values of the nodes.

Strategy Overview:
1. **Find the Middle of the Linked List:**
   - Use the slow and fast pointer technique:
     - `slow` moves one step at a time.
     - `fast` moves two steps at a time.
   - When `fast` reaches the end, `slow` will be at the midpoint.

2. **Reverse the Second Half:**
   - Reverse the list starting from the middle node.
   - This is done in-place using pointer manipulation.

3. **Merge the Two Halves:**
   - Interleave the nodes of the first half and the reversed second half.
   - Alternate between `first` and `second` pointers.

Why it works:
- The fast-slow pointer approach ensures an efficient middle-finding step.
- Reversing the second half enables the "from-end" reordering.
- Final merge step interleaves elements in desired order.

--> Time Complexity:
- O(n): Single traversal to find the middle, reverse, and merge.

--> Space Complexity:
- O(1): In-place operations with only pointer variables used.

'''
class ListNode:
    def __init__(self, val:int = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        #Find the middle
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #Reverse the second half
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        #Merge two halves
        first = head
        second = prev
        while second.next:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
