from typing import List
'''
"Find the duplicate number" — sounds easy, right? Maybe use a set? Nope. Not allowed. 
How about sorting? Too slow. We need **O(1) space** and **linear time**. 
So apparently, the solution is to treat this array like it’s some twisted linked list and use **Floyd’s Tortoise and Hare** algorithm. 
Yes. You heard that right. We're detecting **a cycle**. In an array. What the hell?

--> Time Complexity
O(n), because the pointers will eventually meet. Don’t ask why. Just accept it.

--> Space Complexity
O(1), because using actual tools like a hashmap would be "too easy."

Approach:
- Step 1: Use two pointers (slow and fast) to find a cycle — because this array apparently *loops back on itself like it’s trying to mess with you*.
- Step 2: Reset one pointer and move both at the same speed to find the cycle’s starting point.
  That magically happens to be the duplicate number. No, it doesn’t make intuitive sense. Stop asking.

This problem is the definition of leetcode gaslighting — what looks like a basic question turns into 
some cursed pointer race that only works because someone figured it out and now we all have to pretend it's normal.
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Detect cycle
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        print(slow)
        # Step 2: Find entry point of the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow