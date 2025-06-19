from typing import List
'''
This approach uses binary search to find the minimum element in a rotated sorted array without duplicates.

Base Case:
- If the array is already sorted (no rotation), the first element is the smallest.
- Otherwise, the minimum lies in the unsorted half of the array.

Binary Search Logic:
- If nums[mid] > nums[rp], it means the smallest element lies to the right of mid.
- Else, it lies on the left side or could be the mid itself.

--> Time Complexity

Binary Search Loop:
- The binary search halves the search space in each iteration.
- The loop runs in O(log n), where n is the size of the input array.

Total Time Complexity: **O(log n)**

--> Space Complexity

- No extra space used except a few pointers (lp, rp, mid).
- No recursion or data structures used.

Total Space Complexity: **O(1)**
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp = 0
        rp = len(nums) - 1
        #Base Case
        if nums[rp] > nums[lp]:
                return nums[lp] #Smallest Number

        while rp > lp:
            mid = (lp + rp) // 2
            if nums[mid] > nums[rp]:
                lp = mid +1
            else:
                rp = mid
        
        return nums[lp] 