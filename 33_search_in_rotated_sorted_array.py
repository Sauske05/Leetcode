from typing import List
'''
This approach uses modified binary search to find the target in a **rotated sorted array** without duplicates.

Observation:
- The array is sorted but rotated at an unknown pivot.
- At any point during binary search, **either the left half or the right half must be sorted**.
- Use this to determine which side to eliminate.

Binary Search Logic:
1. If nums[mid] == target → return mid.
2. If right half is sorted (nums[mid] <= nums[rp]):
    - If target is in (mid, rp], move lp = mid + 1
    - Else, move rp = mid - 1
3. If left half is sorted:
    - If target is in [lp, mid), move rp = mid - 1
    - Else, move lp = mid + 1

--> Time Complexity

- Each iteration cuts the search space in half.
- Runs in **O(log n)** time, where n = size of the input array.

--> Space Complexity

- No extra space used except pointers (lp, rp, mid).
- Space Complexity is **O(1)**.

This is optimal for searching in rotated sorted arrays and avoids the need to first find the pivot index separately.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1

        while rp >= lp:
            mid = (lp + rp) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] <= nums[rp]:
                if nums[mid] < target <= nums[rp]:
                    lp = mid + 1
                else:
                    rp = mid - 1
            else:
                if nums[lp] <= target < nums[mid]:
                    rp = mid - 1
                else:
                    lp = mid + 1


        return -1

