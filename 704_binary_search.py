from typing import List
'''
This approach uses the Binary Search algorithm to find the index of the target in a sorted list.

We initialize two pointers, `lp` (left pointer) and `rp` (right pointer), to the start and end of the list respectively.
In each iteration:
- We calculate the middle index `mid` using integer division.
- If `nums[mid]` is greater than the target, we search the left half of the array by updating `rp = mid - 1`.
- If `nums[mid]` is less than the target, we search the right half by updating `lp = mid + 1`.
- If `nums[mid]` equals the target, we return the index `mid`.

If the loop ends without finding the target, we return -1 to indicate it is not present in the list.

--> Time Complexity

Binary Search splits the input space in half on every iteration.

Each step reduces the search space by half → O(log n), where n is the length of the list `nums`.

Total Time Complexity: O(log n)

--> Space Complexity

This algorithm uses constant space — only a few variables (`lp`, `rp`, `mid`) are maintained.

Total Space Complexity: O(1)
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1
        while rp >= lp:
            mid = (lp + rp) // 2
            if nums[mid] > target:
                rp = mid - 1
            elif nums[mid] < target:
                lp = mid + 1
            else:
                return mid
        return -1