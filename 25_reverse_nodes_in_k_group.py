from typing import Optional
# Definition for singly-linked list.
'''
        This approach reverses nodes of a linked list in groups of size k.

        Steps:
        1. Calculate the total length of the linked list (`head_len`) by traversing it once.
        2. Use a dummy node (`dummy_node`) to simplify edge cases and build the result list.
        3. Initialize a pointer (`dummy_node_end`) to track the tail of the merged/reversed list.
        4. Iterate through the list in chunks:
           - For each group, check if enough nodes remain to reverse (i.e., `head_len - total_count >= k`).
           - If not enough nodes remain, link the rest of the list as-is and break.
           - Otherwise, reverse the next k nodes:
             - Use three pointers (`prev`, `curr`, and `temp`) to reverse the nodes in-place.
             - Update `total_count` to keep track of how many nodes have been processed.
           - Attach the reversed segment to the end of the result list.
        5. Move `dummy_node_end` pointer to the end of the newly attached reversed group before continuing.

        Why this works:
        - Reversing in chunks of k ensures nodes are only reversed when a full group is available.
        - Using a dummy node simplifies list head management.
        - Carefully tracking `total_count` and list length avoids partial group reversal.

        --> Time Complexity:
        - O(N), where N is the number of nodes, since each node is visited at most twice (once for counting length, once for reversal).

        --> Space Complexity:
        - O(1), as reversal is done in-place without additional data structures.
        '''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_node = ListNode(float('inf'))
        dummy_node_end = dummy_node
        total_count = 0
        head_len = 0
        curr = head
        while curr:
            curr = curr.next
            head_len +=1

        curr = head
        while curr:
            count = 0                
            prev = None
            #start = curr
            if head_len - total_count < k:
                dummy_node_end.next = curr
                break
            else:
                #onlyy then reverse
                while curr and count < k:
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
                    count +=1
                    total_count +=1
                dummy_node_end.next = prev
              
            #Traversee dummyy node till end
            while dummy_node_end.next:
                dummy_node_end = dummy_node_end.next
             
        return dummy_node.next