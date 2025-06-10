from typing import List
'''
For this approach, we construct an output array where each element is the product of all elements in the input list
except the element at that index. We achieve this without using division, by computing prefix and postfix products.

Step-by-step:

1. Initialize an output array of the same size as input, filled with 1s.
2. Traverse from left to right, maintaining a prefix product:
   - At each index, store the product of all elements to the left of that index.
3. Traverse from right to left, maintaining a postfix product:
   - Multiply each output[i] with the product of all elements to the right of that index.

This ensures that output[i] = prefix_product[i] * postfix_product[i], where prefix_product[i] is the product of all elements before i,
and postfix_product[i] is the product of all elements after i.

--> Time Complexity

Left-to-right loop: O(n)  
Right-to-left loop: O(n)  
Each element is visited twice (once for prefix and once for postfix).

Total Time Complexity: O(n)

--> Space Complexity

Output List: O(n)  
Prefix and postfix use constant space (just two variables).

Total Space Complexity: O(n)
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix = 1
        post_fix = 1
        for i in range(1, len(nums)):
            prefix *= nums[i-1]
            output[i] = prefix
        #print(output)
        for i in range(len(nums)-2, -1, -1):
            post_fix *= nums[i+1]
            output[i] *= post_fix

        #print(output)
        return output
