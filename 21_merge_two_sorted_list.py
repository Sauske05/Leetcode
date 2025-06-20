from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
This approach merges two sorted linked lists into a single sorted linked list.

1. We use a dummy node as the starting point to simplify pointer management.
2. Two pointers, l1 and l2, iterate over list1 and list2 respectively.
3. At each step, the node with the smaller value is selected and appended to the new list.
4. After one of the lists is fully traversed, we attach the remaining part of the other list.
5. The result is a sorted linked list containing all nodes from both input lists.

Note: New `ListNode` instances are created while merging for the smaller value comparison,
but leftover nodes are directly attached without creating new nodes.

--> Time Complexity

We traverse each node in list1 and list2 exactly once.

If list1 has `n` nodes and list2 has `m` nodes, the loop runs O(min(n, m)) times,
and the final linking of the remaining part adds up to O(n + m).

Total Time Complexity: O(n + m)

--> Space Complexity

We create new nodes only when comparing values (not when appending the tail),
so the space overhead from new node creation is O(min(n, m)).

If we instead reused existing nodes throughout (without creating `ListNode(l1.val)`), it would be O(1) space.

Total Space Complexity: O(min(n, m)) [in current form]
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(float('-inf'))
        current_ptr = dummy_node
        l1 = list1 #Pointer for list1 head
        l2 = list2 #Pointer for list2 head
        while l1 and l2:
            if l1.val > l2.val:
                current_ptr.next = ListNode(l2.val)
                l2 = l2.next
            else:
                current_ptr.next = ListNode(l1.val)
                l1 = l1.next
            current_ptr = current_ptr.next


        #Extend l1 l2 if it remains
        if l1:
            current_ptr.next = l1
        if l2:
            current_ptr.next = l2
            
        return dummy_node.next